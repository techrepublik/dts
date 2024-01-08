from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

class Agency(models.Model):
    agency_name = models.CharField(max_length=50)
    ageny_address = models.CharField(max_length=50)
    agency_head = models.CharField(max_length=50)
    agency_contact = models.CharField(max_length=50)
    agency_email = models.CharField(max_length=50)
    agency_website = models.CharField(max_length=50)
    agency_logo1 = models.ImageField(upload_to='static/dist/img/agency_logo',blank=True,null=True)
    agency_logo2 = models.ImageField(upload_to='static/dist/img/agency_logo',blank=True,null=True)
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.agency_name

class Office(models.Model):
    office_name = models.CharField(max_length=50, blank = True, null= True)
    office_head = models.CharField(max_length= 50)
    office_description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    agency = models.ForeignKey(Agency,related_name="office_agency_name",on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.office_name}'
        return template.format(self)


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    office_user = models.BooleanField(default=False)

    
    def __str__(self):
        template = '{0.first_name} {0.middle_name} {0.last_name}'
        return template.format(self)
     
class Office_user_Manager(BaseUserManager):
    def get_queryset(self, *args, **kwargs):
        results = super().get_queryset(*args, **kwargs)
        return results.filter(office_user=True)


class Office_User(User):

    personel = Office_user_Manager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.office_user = True
            self.is_staff = True
            self.is_active = True
            self.is_superuser = False
            
            return super().save(*args, **kwargs)
    
    def welcome(self):
        return "Only for office user"
    
@receiver(post_save, sender= Office_User)
def create_user_profile(sender, instance, created, **kwargs):
    if created and instance.office_user == True:
        Office_User_Profile.objects.create(user=instance)


class Office_User_Profile(models.Model):
    user = models.ForeignKey(User, related_name = 'office_user_name', on_delete = models.CASCADE)
    office = models.ForeignKey(Office, related_name='user_office_name', on_delete = models.CASCADE, blank=True,null=True)
    department = models.CharField(max_length = 50, blank = True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    
    
    

    



