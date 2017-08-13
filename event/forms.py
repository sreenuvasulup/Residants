from __future__ import unicode_literals
from django.shortcuts import redirect

from collections import OrderedDict
from django import forms
from .models import *
import pdb
from django.contrib.auth.models import User


class EventCreationForm(forms.ModelForm):
    """
        This Form used to Save Event Details along with Buildings and Residants
    """
    buildings = forms.ModelMultipleChoiceField(queryset=Buildings.objects.all())
    residants = forms.ModelMultipleChoiceField(queryset=Residants.objects.all())

    class Meta:
        model = Event
        fields = ("create_by","title","description","datetime")

    def save(self, commit=True):
        """
            Save and Return an object details of Event
            Based On Selection of Buildings and Residants,it will save details M2M Relations
        """
        data = self.cleaned_data
        event = super(EventCreationForm, self).save(commit=True)
        if event is not None:
            has_buildings = [EventHasBuildings(event=event,building=item) for item in data.get('buildings',[])]
            has_residants = [EventHasResidants(event=event,residant=item) for item in data.get('residants',[])]
            if len(has_buildings) > 0: EventHasBuildings.objects.bulk_create(has_buildings)
            if len(has_residants) > 0: EventHasResidants.objects.bulk_create(has_residants)
        return event

    def save_m2m(self):
        return True
