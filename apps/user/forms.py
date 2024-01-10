from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Office_User,User,Office_User_Profile, Agency, Department, Office

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "first_name",
                "class": "form-control"
            }
        ))
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "middle_name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "last_name",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Office_User
        fields = ('username','first_name','middle_name','last_name', 'password1', 'password2')


class AdminSignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Username",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "first_name",
                "class": "form-control"
            }
        ))
    middle_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "middle_name",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "last_name",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Password check",
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username','first_name','middle_name','last_name', 'password1', 'password2')


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = Office_User_Profile
        fields = ['office','department','picture']



class AgencyForm(forms.ModelForm):
    class Meta:
        model = Agency
        fields = ['agency_name','agency_address','agency_head', 'agency_contact','agency_email','agency_website','agency_logo1','agency_logo2',]
        # josh Jan 10, 2024
        widgets = {
            'agency_name': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Agency name'}),
            'agency_address': forms.Textarea(attrs={'rows': 3, 'class': 'form-control-sm', 'placeholder': 'Enter an address'}),
            'agency_head': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Head'}),
            'agency_contact': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Contact'}),
            'agency_email': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Email'}),
            'agency_website': forms.TextInput(attrs={'class':'form-control-sm', 'placeholder': 'Website url (www.delta-ph.com)'}),
        }


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['department_name',]

class OfficeForm(forms.ModelForm):
    class Meta:
        model = Office
        fields = ['office_name','office_head','office_branch','office_description','agency',]