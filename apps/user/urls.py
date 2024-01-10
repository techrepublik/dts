from django.urls import path

from . import views

urlpatterns = [
    path('user/index', views.office_user_index, name='officeUser-index'),
    path('office/signup', views.office_user_signup, name='officeUser-signup'),
    path('admin/signup', views.admin_user_signup, name='adminUser-signup'),
    path('user/edit_profile', views.office_user_profile, name='user-profile'),
    path('admin/agenncy-list', views.agency_list, name ='agency-list'),
    path('', views.login_view, name ='login'),


     #agency
    path('agencies/', views.agencies, name='agencies'),
    path('agency/add_agency/', views.add_agency, name='add-agency'),
    path('agency/<int:pk>/edit/', views.edit_agency, name='edit-agency'),
    path('agency/<int:pk>/delete/', views.delete_agency, name='delete-agency'),

    #department
    path('departments/', views.departments, name='departments'),
    path('department/add_department/', views.add_department, name='add-department'),
    path('department/<int:pk>/edit/', views.edit_department, name='edit-department'),
    path('department/<int:pk>/delete/', views.delete_department, name='delete-department'),

    #office
    path('officies/', views.officies, name='officies'),
    path('office/add_office/', views.add_office, name='add-office'),
    path('office/<int:pk>/edit/', views.edit_office, name='edit-office'),
    path('office/<int:pk>/delete/', views.delete_office, name='delete-office'),
]
