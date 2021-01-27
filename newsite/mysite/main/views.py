from django.shortcuts import render
from django.http import HttpResponse
import requests
from subprocess import run, PIPE
import sys
import os 
from calculate import *

# Create your views here.
def index(response):
	return render(response, "main/base.html", {})

def all(response):
	return render(response, "main/all.html", {})

def results(response):
	return render(response, "main/results.html", {})

# def output(request):
# 	age = request.POST.get("age")
# 	out = run(sys.executable, ['//HemoPheno//HemoPheno4HF//newsite//mysite//main//HemoPheno4HF.py', age], shell=False, stout=PIPE)

# 	print(out)

# 	return render(request,'main/base.html',{'data1':out})

# def output(request):
# 	data = requests.get("https://reqres.in/api/users")
# 	print(data.text)
# 	data = data.text
# 	return render(request,"main/base.html",{'data':data})

def external(request):
	# input = {}
	# input['age'] = request.POST.get('age')
	# input['ejf'] = request.POST.get('ef')
	# input['hr'] = request.POST.get('hr')
	# input['dia'] = request.POST.get('dia')
	# input['sys'] = request.POST.get('sys')
	# input['rap'] = request.POST.get('rap')
	# input['pas'] = request.POST.get('pas')
	# input['pad'] = request.POST.get('pad')
	# input['pamn'] = request.POST.get('pamn')
	# input['pcwp'] = request.POST.get('pcwp')
	# input['pcwpmn'] = request.POST.get('pcwp_mn')
	# input['co'] = request.POST.get('co')
	# input['ci'] = request.POST.get('ci')
	# input['mixed'] = request.POST.get('mixed')
	# input['mpap'] = request.POST.get('mpap')
	# input['cpi'] = request.POST.get('cpi')
	# input['pp'] = request.POST.get('pp')
	# input['ppp'] = request.POST.get('ppp')
	# input['papp'] = request.POST.get('papp')
	# input['svr'] = request.POST.get('svr')
	# input['rat'] = request.POST.get('rat')
	# input['ppratio'] = request.POST.get('pprat')
	# input['papi'] = request.POST.get('papi')
	# input['sapi'] = request.POST.get('sapi')
	# input['cpp'] = request.POST.get('cpp')
	# input['praprat'] = request.POST.get('praprat')
	# input['testparam'] = request.POST.get('testparam')
	results = run([sys.executable, '/Users/jdano/Documents/HemoPheno/HemoPheno4HF/newsite/mysite/main/calculate.py'], shell=False, stdout=PIPE)
	# print(results)
	# return render(request, "main/results.html", {"score":results,"path":path})
	return render(request, "main/results.html", {"score":results})
