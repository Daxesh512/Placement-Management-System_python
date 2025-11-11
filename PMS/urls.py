"""PMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/stable/topics/http/urls/
"""

from django.urls import path, include
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('company/', include('company.urls')),
    path('student/', include('student.urls')),
    path('', include('home.urls')),   # root URL points to home app
]

# If you want a static template instead of home.urls, uncomment this line:
# path('', TemplateView.as_view(template_name='pms_index.html')),
