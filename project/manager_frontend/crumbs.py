# -*- coding: utf-8 -*-
"""
Application Crumbs
"""
from breadcrumbs import BreadcrumbsMixin
from django.utils.translation import gettext_lazy

site.update({
    'manager:home': gettext_lazy('Home'),
    'manager:bios': gettext_lazy('Bios'),
	'manager:configes': gettext_lazy('ES Configuration'),
    'manager:config': gettext_lazy('RetroArch Configuration'),
	'manager:configas': gettext_lazy('Autostart Script'),
    'manager:logs': gettext_lazy('Logs'),
    'manager:monitoring': gettext_lazy('Monitoring'),
    'manager:roms-systems': gettext_lazy('Rom by system'),
    'manager:roms-list': gettext_lazy('{{ system_name }}'),
    #'manager:roms-saves-list': gettext_lazy('Saves'),
})
