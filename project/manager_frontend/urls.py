app_name = 'manager'

#from django.conf.urls import url
from django.urls import re_path, path
from django.views.generic import TemplateView

from .views import HomeView
from .views.config import RecalboxConfigFormView
from .views.configes import RecalboxConfigEsFormView
from .views.configas import RecalboxConfigAsFormView
from .views.logs import LogsView
from .views.bios import BiosListView, BiosUploadJsonView
from .views.roms import RomListView, RomUploadJsonView
#from .views.saves import SavesListView
from .views.systems import SystemsListView
from .views.monitor import MonitoringView

urlpatterns = [
   re_path (r'^$', HomeView.as_view(), name='home'),
    
    re_path(r'^bios/$', BiosListView.as_view(), name='bios'),
    re_path(r'^bios/upload$', BiosUploadJsonView.as_view(), name='bios-upload'),
    
    re_path(r'^config/$', RecalboxConfigFormView.as_view(), name='config'),
	
	re_path(r'^configes/$',  RecalboxConfigEsFormView.as_view(), name='configes'),
	
	re_path(r'^configas/$',  RecalboxConfigAsFormView.as_view(), name='configas'),
    
    re_path(r'^monitoring/$', MonitoringView.as_view(), name='monitoring'),
    
    re_path(r'^logs/$', LogsView.as_view(), name='logs'),
    
    re_path(r'^systems/$', SystemsListView.as_view(), name='roms-systems'),
    
    #re_path(r'^systems/roms/saves/$', SavesListView.as_view(), name='roms-saves-list'),
    
    re_path(r'^systems/roms/(?P<system>[-\w]+)$', RomListView.as_view(), name='roms-list'),
    re_path(r'^systems/roms/(?P<system>\w+)/$', RomListView.as_view(), name='roms-list'),
    re_path(r'^systems/roms/(?P<system>[-\w]+)/upload/$', RomUploadJsonView.as_view(), name='roms-upload'),

]
