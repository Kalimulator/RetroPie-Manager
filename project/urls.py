"""recalbox-manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import TemplateView
from django.views.static import serve

# Load asset manifest in memory
from project import assets_cartographer
assets_cartographer.autodiscover()

# Load Recalbox manifest in memory
from project import recalbox_manifest
recalbox_manifest.autodiscover()

urlpatterns = [
    # Admin panel
    path('admin/', admin.site.urls),
    
    # Manager frontend
    path('', include('project.manager_frontend.urls', namespace='manager')),
    
    # API (uncomment if needed)
    # path('api/', include('project.api.urls', namespace='api')),
]

# Debug settings
if settings.DEBUG:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True,
        }),
        path('500/', TemplateView.as_view(template_name="500.html")),
        path('404/', TemplateView.as_view(template_name="404.html")),
        path('', include('django.contrib.staticfiles.urls')),
    ]

