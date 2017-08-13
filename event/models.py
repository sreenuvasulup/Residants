# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone
# Create your models here.

class Buildings(models.Model):
    """
        This Model Defines as Building and Details
    """
    name = models.CharField(max_length=250)
    address = models.TextField(blank=True)
    owner = models.ForeignKey(User)

    def __str__(self): return str(self.name)

class Residants(models.Model):
    """
        This Model Specifies Residant Details with Building
    """
    name = models.CharField(max_length=250)
    address = models.TextField(blank=True)
    building_name = models.ForeignKey(Buildings)

    def __str__(self): return str(self.name)

class Event(models.Model):
    """
        This Model have all Event Details
    """
    create_by = models.ForeignKey(User)
    title = models.CharField(max_length=250)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now=False,auto_now_add=False)

    def __str__(self): return str(self.title)

class EventHasResidants(models.Model):
    """
        This Model act like connection b/w event and residants.
        Event will be conducted for all or Specific Residants
    """
    event = models.ForeignKey(Event)
    residant = models.ForeignKey(Residants)

    def __str__(self): return str(self.event)

class EventHasBuildings(models.Model):
    """
        This Model act like connection b/w event and buildings
        Event will be conducted for all or Specific Buildings
    """
    event = models.ForeignKey(Event)
    building = models.ForeignKey(Buildings)

    def __str__(self): return str(self.event)
