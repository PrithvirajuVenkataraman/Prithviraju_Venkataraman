# contact_details/urls.py
from django.urls import path
from .views import contact_list, contact_detail, contact_create, contact_edit, contact_delete

urlpatterns = [
    path('', contact_list, name='contact_list'),
    path('contacts/form', contact_detail, name='contact_detail'),
    path('contacts/<int:pk>/edit/', contact_edit, name='contact_edit'),
    path('contacts/<int:pk>/delete/', contact_delete, name='contact_delete'),
    path('contacts/<int:pk>/create/', contact_create, name='contact_update'),
]

