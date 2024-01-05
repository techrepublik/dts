from django.db import models

class Agency(models.Model):
    agency_name = models.CharField(max_length=50)
    ageny_address = models.CharField(max_length=50)
    agency_head = models.CharField(max_length=50)
    agency_contact = models.CharField(max_length=50)
    agency_email = models.CharField(max_length=50)
    agency_website = models.CharField(max_length=50)
    agency_logo1 = models.ImageField(upload_to='static/dist/img/img_user',blank=True,null=True)
    agency_logo2 = models.ImageField(upload_to='static/dist/img/img_user',blank=True,null=True)
    created_at = models.DateTimeField()

    def __str__(self) -> str:
        return self.agency_name
    
class Office(models.Model):
    office_name = models.CharField(max_length=50)
    office_head = models.CharField(max_length= 50)
    office_description = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    agency = models.ForeignKey(Agency,related_name="office_agency_name",on_delete=models.CASCADE)

    def __str__(self):
        template = '{0.office_name}'
        return template.format(self)