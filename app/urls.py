from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('dws-admin/', admin.site.urls),
    path('',include('catalog.urls')),
]
