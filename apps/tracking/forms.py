from django import forms
from . models import  Flow,Attachment,Status, Workflow, Category , Document, Forwarded
import random

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

class WorkflowForm(forms.ModelForm):
    class Meta:
        model = Workflow
        fields = ['office_id', 'flow_id',]

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['document_code', 'document_title', 'document_description', 'document_tags', 'document_pages','category_id','flow',]
        widgets = {
            'document_code': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Document Code'}),
            'document_title': forms.TextInput(attrs={'rows': 3, 'class': 'form-control-sm', 'placeholder': 'Enter Document Title'}),
            'document_description': forms.Textarea(attrs={'class':'form-control-sm', 'placeholder': 'Description'}),
            'document_tags': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'tags'}),
            'document_pages': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'number of pages'}),
            'category_id': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'select category'}),
            'flow': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'select flow'}),
        }

class ForwardedForm(forms.ModelForm):
    class Meta:
        model = Forwarded
        fields = ['document_code','forwarded_from','forwarded_to']

class ConfirmReceiveForm(forms.ModelForm):
    class Meta:
        model = Forwarded
        fields = ['received',]