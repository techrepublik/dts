from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    #category julius/01/10/24
    path('categories/', views.categories, name='categories'),
    path('category/add_category/', views.add_category, name='add-category'),
    path('category/<int:pk>/edit/', views.edit_category, name='edit-category'),
    path('category/<int:pk>/delete/', views.delete_category, name='delete-category'),

    #flow julius/01/11/24
    path('flows/', views.flows, name='flows'),
    path('flow/add_flow/', views.add_flow, name='add-flow'),
    path('flow/<int:pk>/edit/', views.edit_flow, name='edit-flow'),
    path('flow/<int:pk>/delete/', views.delete_flow, name='delete-flow'),

    #status julius/01/11/24
    path('status/', views.status, name='status'),
    path('status/add_status/', views.add_status, name='add-status'),
    path('status/<int:pk>/edit/', views.edit_status, name='edit-status'),
    path('status/<int:pk>/delete/', views.delete_status, name='delete-status'),

    #workflow julius/01/11/24
    path('workflow/', views.workflow, name='workflow'),
    path('workflow/add_workflow/', views.add_workflow, name='add-workflow'),
    path('workflow/<int:pk>/edit/', views.edit_workflow, name='edit-workflow'),
    path('workflow/<int:pk>/delete/', views.delete_workflow, name='delete-workflow'),

    #documents julius/01/12/24
    path('submit_docs/', views.submit_new, name= 'submit-new'),
]
