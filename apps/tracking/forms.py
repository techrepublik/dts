from django import forms
from . models import  Flow,Attachment,Status, Workflow, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name',]

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['status_name', 'status_description',]

class FlowForm(forms.ModelForm):
    class Meta:
        model = Flow
        fields = ['flow_name', 'flow_is_active',]

class AttachmentForm(forms.ModelForm):
    class Meta:
        model = Attachment
        fields = ['attachment_note', 'attachment_file', 'document_id', 'urgency',]
