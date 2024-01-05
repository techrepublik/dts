from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from apps.tracking.models import Office


class User(AbstractUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    middle_name = models.CharField(max_length=20, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(upload_to='static/dist/img/img_user',blank=True,null=True)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    office_user = models.BooleanField(default=False)
    office = models.ForeignKey(Office, related_name='user_office_name', on_delete=models.CASCADE,blank=True,null=True)

    
    
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
        return "Only for User"
    

