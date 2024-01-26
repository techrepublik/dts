from django.contrib import admin
from .models import Document, Forwarded, Received

admin.site.register(Document)


@admin.register(Forwarded)
class Forwarded_Admin(admin.ModelAdmin):
    list_display = ('document_code', 'forwarded_from', 'forwarded_to','date_time','received')
@admin.register(Received)
class Received_Admin(admin.ModelAdmin):
    list_display = ('document_code','date_time',)