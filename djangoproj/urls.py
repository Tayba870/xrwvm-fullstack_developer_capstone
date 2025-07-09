"""djangoproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Admin site
    path('admin/', admin.site.urls),
    
    # Main app routes
    path('djangoapp/', include('djangoapp.urls')),
    
    # Static pages
    path('', TemplateView.as_view(template_name="Home.html"), name='home'),
    path('about/', TemplateView.as_view(template_name="About.html"), name='about'),
    path('contact/', TemplateView.as_view(template_name="Contact.html"), name='contact'),
    
    # API routes (if needed)
    # path('api/', include('api.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)