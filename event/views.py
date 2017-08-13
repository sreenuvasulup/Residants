# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from django.http import JsonResponse

# Create your views here.

def getResidantsByBuilding(request):
    """
    :param request: accept Request From ajax
    :return:  all Residants Based On Building Selection
    """
    building_ids = [int(i) for i in request.GET.get('data', "").split(',')]
    data = {}
    if building_ids is not None:
        data["list_data"] = [{"id":i["id"],"name":i["name"]} for i in Residants.objects.filter(building_name_id__in=building_ids).values("id","name")]
        data["success"] = True
    else:
        data['error_message'] = 'Invalid Selection or Emptyuser with this username already exists.'
    return JsonResponse(data)


