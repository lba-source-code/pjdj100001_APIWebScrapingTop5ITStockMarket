"""DSSi comment: standard package """
from django.urls import path

from . import views

urlpatterns = [
    path('', views.srv_scraper_stockmarket)
]