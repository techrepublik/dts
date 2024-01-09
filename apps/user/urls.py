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
    path('agency/<int:pk>/update/', views.edit_agency, name='edit-agency'),
    path('agency/<int:pk>/delete/', views.delete_agency, name='delete-agency'),
]
