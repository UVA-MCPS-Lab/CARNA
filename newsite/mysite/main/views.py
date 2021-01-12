from django.shortcuts import render
from django.http import HttpResponse
from .forms import invasive

# Create your views here.
def index(response):
	return render(response, "main/base.html", {})

def all(response):
	return render(response, "main/all.html", {})

def form(response):
	if response.method == "POST":
		form = invasive(response.POST)

		if form.is_valid():
			n = form.cleaned_data["name"]

		return HttpResponse(n)

	else: 
		form = invasive()

	form = invasive()
	return render(response, "main/form.html", {"form":form})
