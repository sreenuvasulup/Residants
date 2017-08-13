from django.conf.urls import url
from .views import getResidantsByBuilding

"""
	These Urls are Belongs To Event App
"""

urlpatterns = [
	url(r'^getResidants/$', getResidantsByBuilding, name='residants-list'),
	]
