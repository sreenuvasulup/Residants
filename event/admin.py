# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from .forms import EventCreationForm

from django.contrib import admin

# Register your models here.
class ResidantsAdmin(admin.ModelAdmin):
	model = Residants
	# list_display = ('user','display_name')
	# list_filter = ('user','display_name')

class ResidantsInline(admin.TabularInline):
    """
        Residants inline
    """
    fieldsets = (
        (
            None,
            {
                'fields': ('name', 'address',)
            }
        ),
    )
    model = Residants
    extra = 1



class EventAdmin(admin.ModelAdmin):
    model = Event
    add_form = EventCreationForm

    def get_form(self, request, obj=None, **kwargs):
        """
		Use special form during user creation
		"""
        defaults = {}
        if obj is None:
            defaults['form'] = self.add_form
        defaults.update(kwargs)
        return super(EventAdmin, self).get_form(request, obj, **defaults)


class BuildingsAdmin(admin.ModelAdmin):
    model = Buildings
    inlines = (ResidantsInline, )

class EventHasResidantsAdmin(admin.ModelAdmin):
    model = EventHasResidants

class EventHasBuildingsAdmin(admin.ModelAdmin):
    model =  EventHasBuildings


admin.site.register(Residants, ResidantsAdmin)
admin.site.register(Event,EventAdmin)
admin.site.register(EventHasResidants,EventHasResidantsAdmin)
admin.site.register(EventHasBuildings,EventHasBuildingsAdmin)
admin.site.register(Buildings,BuildingsAdmin)
