from django.contrib import admin
from .models import Document, Forwarded, Received, Model1

# 2024-03-02 josh
@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display=('document_code','document_title','document_description','user')


@admin.register(Forwarded)
class Forwarded_Admin(admin.ModelAdmin):
    list_display = ('document_code', 'forwarded_from', 'forwarded_to','date_time')

@admin.register(Received)
class Received_Admin(admin.ModelAdmin):
    list_display = ('document_code','date_time',)

@admin.register(Model1)
class Model1_Admin(admin.ModelAdmin):
    list_display = ('name',)