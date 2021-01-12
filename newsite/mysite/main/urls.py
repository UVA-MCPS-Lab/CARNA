from django.urls import path
from . import views

urlpatterns = [
path("", views.index, name="index"),
path("all/", views.all, name="all"),
path("form/", views.form, name="form"),
]
