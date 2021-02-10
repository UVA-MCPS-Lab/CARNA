from django.urls import path
from . import views
from .util.MVDD import *

urlpatterns = [
	path("", views.index, name="index"),
	path("all/", views.all, name="all"),
	path("results/", views.results, name="results"),
	path("external", views.external, name="script"),
]
