import json
import itertools

#assuming search results are provided in json according to DATS
#had to use a highly simplified, made up data set for development
#this code loads the search results
with open('search_results.json') as f:
    data = json.load(f)

#this code creates a dictionary of results that incorporates the important elements
#that are likely to be the same between equivalent data sets
#the key is a number
#the value is the list of important elements
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

#create a list of the keys in the dictionary of results
#this should be a list of numbers
y = list(results.keys())

#create a list of all possible pairwise combinations of the dictionary keys
#all duplication is removed
z = itertools.combinations(y,2)

#using the list of all key combinations, compare the values
#return a list of equivalent identifiers as tuples
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
		equiv.append((id_a,id_b))
print(equiv)
