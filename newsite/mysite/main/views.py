from django.shortcuts import render
from django.http import HttpResponse
import requests
from subprocess import run, PIPE
import sys
import os 
from .util.calculate import *
from .util.MVDD import *
from .util.Main import *

# Create your views here.
def index(response):
	return render(response, "main/base.html", {})

def all(response):
	return render(response, "main/all.html", {})

def results(response):
	return render(response, "main/results.html", {})

def external(request):
	class MVDD:
		def __init__(self, features, dot, root=None, model=None, featureDict={}):
			self.features = features #list of features
			self.dot = dot #network x graph, representing MVDD
			self.root = root #root node of tree
			self.featureDict = featureDict #feature dictionary with ranges for each of the features
			self.model = model
			self.terminalIndices = None

		# Save graph to file in specific format
		# INPUT = filename and format
		# OUTPUT = saved graph file in specified format
		def saveToFile(self, filename='mvdd', format='pdf'):
			dt = to_pydot(self.dot)

			if format == "png":
				dt.write_png(filename + '.png')
			else:
				dt.write_pdf(filename + '.pdf')

		# Save dot file for MVDD graph
		# INPUT = filename
		# OUTPUT = .dot file of networkx graph
		def saveDotFile(self, filename='mvdd'):
			dt = to_pydot(self.dot)
			dt.write_dot(filename + ".dot")

		# Traverses dot graph in MVDD
		# INPUT = N/A
		# OUTPUT = N/A
		def traverseGraph(self):
			dot = self.dot
			for n in nx.bfs_edges(dot, 'PCWPMod'):
				print(n)
				nodeName = n[0]
				print(dot.nodes[nodeName])

			print("edges connected to node", dot.edges('PCWPMod'))
			print(dot.get_edge_data('PP', 'PAPP'))  # get label and style of edge

			# UPDATE LABEL LIKE THIS
			dot.edges['PP', 'PAPP', 0]['label'] = 'New Label'
			print("\n\n", dot.edges['PP', 'PAPP', 0])

			# self.saveToFile(dot, "NewTEST")
			# print(dot.get_edge_data('PP', 'PAPP'))  # get label and style of edge

		# Return dictionary of node and number edges
		# INPUT = if want to return terminal nodes
		# OUTPUT = dictionary of node and number edges
		def getNumberBranchesPerNode(self, returnTerminals=False):
			dct = {}
			for n in nx.nodes(self.dot):
				if returnTerminals:
					dct[n] = len(self.dot.edges(n))
				else:
					if n not in ['1', '2', '3', '4', '5']:
						dct[n] = len(self.dot.edges(n))

			return dct

		# Predicts score from a single dictionary of feature values
		# INPUT = feature dictionary of actual data values
		# OUTPUT = predicted score and the final path illustrating the used phenotype
		def predictScore(self, xData):
			predScore = self.model.predict(xData)[0]

			path = self.getDecisionPath(self.terminalIndices, predScore, xData)
			# path = None
			# for p in paths:
			#     truthVal, score = self.evaluatePathValue(p, xData)
			#     if score == predScore:
			#         path = p
			#         break

			# self.getDecisionPath(xData)
			# tree_rules = export_text(self.model, feature_names=list(xData))
			# print(tree_rules)

			return predScore, path


		#Get all tree paths from root
		# INPUT = N/A
		# OUTPUT = returns a list of all paths through the mvdd dot tree
		def getDecisionPath(self, terminalIndices, score, xData):
			allPaths = []

			for t in terminalIndices:
				for p in self.all_simple_paths(self.dot, self.root, t):

					featureList = []

					#get score
					label = self.dot.nodes[p[-1]]['label']
					label = label.replace("\"", "")
					cls = label.split('\\n')[-1]
					cls = cls.replace("class = ", "")

					if str(cls) == str(score):
						for i in range(len(p)-1):
							label = self.dot.nodes[p[i]]['label']
							label = label.replace("\"", "")
							ft = label.split('\\n')[0]
							featureList.append(ft)

						allPaths.append(featureList)

			#get exact path
			# print(allPaths)
			return allPaths[0]

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

	# results = runHemo(input, request.POST.get('testparam'))
	# stringy = results[0]
	# score = results[1]
	# path = results[2]
	# print(stringy, score, path)

	string, score, path = get_results(input, request.POST.get('testparam'))
	# string = "hello"
	# score = 1
	# outcome = "DEATH"	
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

