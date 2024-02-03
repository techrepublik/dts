from django.db import models
import uuid,secrets
from apps.user.models import User, Office_User, Office, Agency
from django.db.models.signals import post_save
from django.dispatch import receiver

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.category_name

class Flow(models.Model):
    flow_name = models.CharField(max_length=50)
    flow_is_active = models.BooleanField()
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.flow_name

def random():
    return secrets.token_hex(4)
    
class Document(models.Model):
    document_code = models.CharField(max_length=50, default=random,unique=True,)
    document_title = models.CharField(max_length=50)
    document_description= models.CharField(max_length=50)
    document_tags = models.CharField(max_length=50)
    document_pages = models.IntegerField()
    category_id = models.ForeignKey(Category,related_name='category_of_document',on_delete=models.CASCADE, null =True, blank=True)
    flow = models.ForeignKey(Flow,related_name='document_flow_name',on_delete=models.CASCADE,null =True, blank =True)
    user = models.ForeignKey(User, related_name='document_user', on_delete=models.CASCADE, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.document_code}'
        return template.format(self)

@receiver(post_save, sender= Document)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Tracking.objects.create(document=instance)
    
class Tracking(models.Model):
    document= models.ForeignKey(Document,related_name='document_tracking',on_delete=models.CASCADE)
    tracking_note= models.CharField(max_length=50)
    tracking_priority= models.CharField(max_length=50)
    # status = models.ForeignKey(Status,related_name='status_tracking',on_delete=models.CASCADE)
    # office_user= models.ForeignKey(Office_User,related_name='office_user_tracking',on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.document
    
class Forwarded(models.Model):
    document_code= models.ForeignKey(Document,related_name='forward_document',on_delete=models.CASCADE)
    forwarded_from = models.ForeignKey(Office, related_name = 'forward_from_office', on_delete =models.CASCADE, null = True, blank = True)
    forwarded_to = models.ForeignKey(Office, related_name = 'forward_to_office', on_delete =models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)
    received = models.BooleanField(default =False)

    def __str__(self):
        template = '{0.document_code}'
        return template.format(self)
    
@receiver(post_save, sender= Forwarded)
def create_user_profile(sender, instance, created, **kwargs):
    if instance.received == True:
        Received.objects.create(document_code=instance)


class Received(models.Model):
    document_code = models.ForeignKey(Forwarded,related_name='received_doc',on_delete = models.CASCADE)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        template = '{0.document_code}'
        return template.format(self)

class Status(models.Model):
    status_name = models.CharField(max_length=50)
    status_description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.status_name
    

class Attachment(models.Model):
    attachment_note = models.CharField(max_length=50)
    attachment_file = models.CharField(max_length=50)
    document_id = models.ForeignKey(Document,related_name='document_attachment',on_delete=models.CASCADE)
    urgency = models.ForeignKey(Agency,related_name='agency_attachment',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.attachment_note

class Workflow(models.Model):
    office_id = models.ForeignKey(Office,related_name='office_workflow',on_delete=models.CASCADE)
    sub_office = models.IntegerField(null = True, blank = True)
    flow_id = models.ForeignKey(Flow,related_name='flow_workflow',on_delete=models.CASCADE)
    created_id = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.office_id