from django.db import models
from apps.user.models import User, Office_User, Office, Agency

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.category_name
    
    
class Document(models.Model):
    document_code = models.CharField(max_length=50)
    document_title = models.CharField(max_length=50)
    document_description= models.CharField(max_length=50)
    document_tags = models.CharField(max_length=50)
    document_pages = models.IntegerField()
    category_id = models.ForeignKey(Category,related_name='category_of_document',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document_code
    


class Status(models.Model):
    status_name = models.CharField(max_length=50)
    status_description = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.status_name
    
class Tracking(models.Model):
    tracking_in = models.DateTimeField()
    tracking_out= models.DateTimeField()
    tracking_note= models.CharField(max_length=50)
    tracking_priority= models.CharField(max_length=50)
    status_id = models.ForeignKey(Status,related_name='status_tracking',on_delete=models.CASCADE)
    document_id= models.ForeignKey(Document,related_name='document_tracking',on_delete=models.CASCADE)
    office_user_id= models.ForeignKey(Office_User,related_name='office_user_tracking',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.tracking_in
    

class Attachment(models.Model):
    attachment_note = models.CharField(max_length=50)
    attachment_file = models.CharField(max_length=50)
    document_id = models.ForeignKey(Document,related_name='document_attachment',on_delete=models.CASCADE)
    agency_id = models.ForeignKey(Agency,related_name='agency_attachment',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.attachment_note

class Flow(models.Model):
    flow_name = models.CharField(max_length=50)
    flow_is_active = models.BooleanField()
    created_at =  models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.flow_name


class Workflow(models.Model):
    office_id = models.ForeignKey(Office,related_name='office_workflow',on_delete=models.CASCADE)
    flow_id = models.ForeignKey(Flow,related_name='flow_workflow',on_delete=models.CASCADE)
    created_id = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.office_id