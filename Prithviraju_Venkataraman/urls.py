# Prithviraju_Venkataraman/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contacts/', include('contact_details.urls')),
    
]
