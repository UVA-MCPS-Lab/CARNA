from django.shortcuts import render
from django.http import HttpResponse
import requests
from subprocess import run, PIPE
import sys
import os 
from .util.calculate import *
from .util.MVDD import *

# Create your views here.
def index(response):
	return render(response, "main/base.html", {})

def all(response):
	return render(response, "main/all.html", {})

def results(response):
	return render(response, "main/results.html", {})

def external(request):
	input = {}
	input['age'] = request.POST.get('age')
	input['ejf'] = request.POST.get('ef')
	input['hr'] = request.POST.get('hr')
	input['bpdias'] = request.POST.get('dia')
	input['bpsys'] = request.POST.get('sys')
	input['rap'] = request.POST.get('rap')
	input['pas'] = request.POST.get('pas')
	input['pad'] = request.POST.get('pad')
	input['pamn'] = request.POST.get('pamn')
	input['pcwp'] = request.POST.get('pcwp')
	input['pcwpmn'] = request.POST.get('pcwp_mn')
	input['co'] = request.POST.get('co')
	input['ci'] = request.POST.get('ci')
	input['mixed'] = request.POST.get('mixed')
	input['mpap'] = request.POST.get('mpap')
	input['cpi'] = request.POST.get('cpi')
	input['pp'] = request.POST.get('pp')
	input['ppp'] = request.POST.get('ppp')
	input['papp'] = request.POST.get('papp')
	input['svr'] = request.POST.get('svr')
	input['rat'] = request.POST.get('rat')
	input['ppratio'] = request.POST.get('pprat')
	input['papi'] = request.POST.get('papi')
	input['sapi'] = request.POST.get('sapi')
	input['cpp'] = request.POST.get('cpp')
	input['praprat'] = request.POST.get('praprat')
	input['testparam'] = request.POST.get('testparam')
	# results = run([sys.executable, '/Users/jdano/Documents/HemoPheno/HemoPheno4HF/newsite/mysite/main/calculate.py'], shell=False, stdout=PIPE)
	string = ""
	score = 0
	path = "" 

	# string, score, path = get_results(input)
	string = "hello"
	score = 1
	outcome = "DEATH"	
	chance = ""
	color = ""
	if score == 1:
		chance = "LOW"
		color = "green"
	elif score == 2:
		chance = "LOW INTERMEDIATE"
		color = "lime"
	elif score == 3:
		chance = "INTERMEDIATE"
		color = "yellow"
	elif score == 4:
		chance = "INTERMEDIATE HIGH"
		color = "orange"
	else:
		chance = "HIGH"
		color = "red"

	desc = "Given the inputted data, the algorithm has returned a score of " + str(score) + ", which means that the risk level is " + chance + ". This score indicates that the patient has a less than 10% chance of the outcome: " + str(outcome)
	path = "PCWP <= 18.5 | HRTRT > 26.5 | CPI > 0.497 | PAD > 2.5 | MPAP <= 63.5 | BPSYS <= 85.5 | SVR >= 1690.213"
	# print(results)
	return render(request, "main/results.html", {"score":score, "desc":desc, "path":path, "chance":chance, "color":color})

