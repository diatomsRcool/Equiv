import json
#import numpy as np
import itertools
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

y = list(results.keys())
z = itertools.combinations(y,2)

equiv = []
for p,q in z:
	print(p)
	print(q)
	a = results[p]
	b = results[q]
	id_a = a[0]
	id_b = b[0]
	x = [i for i, j in zip(a, b) if i == j]
	print(x)
	if len(x) == len(a) - 1:
		print(id_a + ' and ' + id_b + ' are equivalent data sets.')
		equiv.append([id_a,id_b])
print(equiv)
