import json
import numpy as np
#import jsoncompare

with open('search_results.json') as f:
    data = json.load(f)

results = {}
for i,d in enumerate(data):
	m = []
	m.append(d['id'])
	m.append(d['relatedIdentifier'])
	m.append(d['date'])
	m.append(d['creator'])
	m.append(d['producedBy'])
	results[i] = m
z = len(data)

for k,v in results.items():
	if k < z - 1:
		counter = 1
		a = results[k]
		b = results[k + counter]
		print([i for i, j in zip(a, b) if i == j])
		counter =+ 1
#y = set(a).intersection(b)
#print(y)
#a = np.equal(results[0],results[1])
#print(a)
"""
if relatedIdentifier[0] == relatedIdentifier[1]:
	if date[0] == date[1]:
		if creator[0] == creator[1]:
			if producedBy[0] == producedBy[1]:
				
if relatedIdentifier[0] == relatedIdentifier[2]:

if relatedIdentifier[1] == relatedIdentifier[2]:

i = len(data)
x = 0

dict_1 = data[0]
dict_2 = data[1]
dict_3 = data[2]
a = dict_1.items() & dict_2.items()
print(a)
print(data[0])
print(type(data[0]))
print(data[0].items())
print(data[1].items())
print(data[0].items() & data[1].items())
print(x)

dict_1,dict_2,dict_3 = sep_results(data)
a = dict_1.items() & dict_2.items()
print(a)

	with open(str(counter) + '.json', 'w') as outfile:
		json.dump(d, outfile)
	counter = counter + 1
	#RID = d['relatedIdentifier']
	#data = d['date']
	#creator = d['creator']
	#producedBy = d['producedBy']
	print(d)

#print(data[0])
def sep_results(data):
	i = 1
	for d in data:
		file = 'dict_%s' % i
		print(file)
		file = d
		print(file)
		i += 1
	return(dict_1,dict_2,dict_3)
	
	dictname = 'dict_%s' % i
	results.append(dictname)
	dictname = d
for r in results:
	print(r)

i = len(data)
id = []
relatedIdentifier = []
date = []
creator = []
producedBy = []
for i,d in enumerate(data:
	id.append(d['id'])
	relatedIdentifier.append(d['relatedIdentifier'])
	date.append(d['date'])
	creator.append(d['creator'])
	producedBy.append(d['producedBy'])
print(relatedIdentifier)
np.equal
if relatedIdentifier[0] == relatedIdentifier[1]:
	if date[0] == date[1]:
		if creator[0] == creator[1]:
			if producedBy[0] == producedBy[1]:
				
if relatedIdentifier[0] == relatedIdentifier[2]:

if relatedIdentifier[1] == relatedIdentifier[2]:

import warnings
import numpy as np
warnings.simplefilter(action='ignore', category=FutureWarning)
"""