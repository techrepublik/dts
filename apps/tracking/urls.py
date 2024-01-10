from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #office
    path('categories/', views.categories, name='categories'),
    path('category/add_category/', views.add_category, name='add-category'),
    path('category/<int:pk>/edit/', views.edit_category, name='edit-category'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete-category'),
]
