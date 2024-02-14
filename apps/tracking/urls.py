from collections import namedtuple
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

    #received
    path('received_docs/', views.received_doc, name= 'received-doc'),

    #forwarded
    path('forwarded_docs/', views.forwarded_doc, name= 'forwarded-doc'),

    #incoming
    path('incoming_docs/', views.incoming, name= 'incoming-doc'),
    path('incoming/<int:pk>/reaceived/', views.confirm_received, name='confirm-received'),

    #new documents2024-02-03 Josh
    path('documents/', views.get_all_documents, name='documents-list'),
    path('documents/add_document/', views.add_document, name='add-document'),
    path('new_doc/forward/', views.doc_new_forward, name='doc-new-forward'),

    #tracking
    path('document/<int:pk>/tracking', views.tracking, name= 'track-doc'),
    path('documents/track/list', views.tracking_doc_list, name= 'track-doc-list'),

    #search
    path('search/', views.search, name='search'),


    ####################################################################################

    path('get-model1-data/<int:pk>/', views.get_model1_data, name='get_model1_data'),
    path('create-model2/', views.create_model2, name='create_model2'),
    path('aa/', views.aaa, name='aaa'),
]
