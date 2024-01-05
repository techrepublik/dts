from django.contrib import admin
from .models import User,Office_User
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ('username', 'first_name','last_name')
    list_filter = ('username', 'first_name', 'office_user',)
    ordering = ('-created_at',)
    list_display = ('username', 'first_name','middle_name','last_name','created_at',
                    'is_superuser','is_active', 'is_staff','office_user')
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','middle_name','last_name','picture')}),
        ('Permissions', {'fields': ('is_superuser','is_staff', 'is_active',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','middle_name','last_name', 'password1', 'password2',)}
         ),
    )

class OfficeUserAdminConfig(UserAdmin):
    model = User
    search_fields = ('email', 'username', 'first_name','last_name')
    list_filter = ('email', 'username', 'first_name', 'is_active', 'is_staff')
    ordering = ('-created_at',)
    list_display = ('email', 'username', 'first_name','middle_name','last_name','created_at',
                    'office_user','is_active', 'is_staff',)
    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name','middle_name','last_name','picture')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'first_name','middle_name','last_name', 'password1', 'password2',)}
         ),
    )

admin.site.register(User,UserAdminConfig)

admin.site.register(Office_User,OfficeUserAdminConfig)
