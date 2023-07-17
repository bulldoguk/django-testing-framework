from django.urls import path

from . import views
from django.urls.resolvers import URLPattern

urlpatterns: list[URLPattern] = [
    path("", views.index, name="index"),
]
