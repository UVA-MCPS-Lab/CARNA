from django.shortcuts import render
from .util.calculate import *


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
	# input['testparam'] = request.POST.get('testparam')
	# results = run([sys.executable, '/Users/jdano/Documents/HemoPheno/HemoPheno4HF/newsite/mysite/main/calculate.py'], shell=False, stdout=PIPE)
	string = ""
	score = 0
	path = "" 

	string, score, path, outcome = get_results(input, request.POST.get('testparam'))
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

	# print(results)
	return render(request, "main/results.html", {"score":score, "desc":desc, "path":str(path), "chance":chance, "color":color})

