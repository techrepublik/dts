from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/page', views.office_user_index, name='officeUser-index'),
    path('login/', views.login_view, name ='login')
]
