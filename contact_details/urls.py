from django.urls import path
from .views import contact_list, contact_detail, contact_create, contact_edit, contact_delete

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('contacts/create/', contact_create, name='contact_create'),
    path('contacts/<int:pk>/edit/', contact_edit, name='contact_edit'),
    path('contacts/<int:pk>/delete/', contact_delete, name='contact_delete'),
]
