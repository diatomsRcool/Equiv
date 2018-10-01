import json
import itertools

#assuming search results are provided in json according to DATS
#had to use a highly simplified, made up data set for development

#this code loads the search results
with open('search_results.json') as f:
    data = json.load(f)

#this code creates a dictionary of results that incorporates the important elements
#that are likely to identify equivalent and related data sets
#the key is a number
#the value is the list of important elements
results = {}
for i,d in enumerate(data):
	m = []
	d.setdefault('relatedIdentifier','')
	d.setdefault('identifier','')
	d.setdefault('producedBy', '')
	m.append(d['@id'])
	m.append(d['relatedIdentifier'])
	m.append(d['datePublished'])
	m.append(d['author'])
	m.append(d['producedBy'])
	n = d['identifier']
	b = {}
	for j in n:
		b.setdefault('propertyID', '')
		b.setdefault('value', '')
		b[j['propertyID']] = j['value']
	m.append(b)
	results[i] = m

#create a list of the keys in the dictionary of results
#this should be a list of numbers
y = list(results.keys())

#create a list of all possible pairwise combinations of the dictionary keys
#all duplication is removed
z = itertools.combinations(y,2)

#this function finds equivalent and related data sets
def relat_test(a,b):
	test = False
	y = None
	id_a = a[0] #this pulls the @id for the two data sets being compared
	id_b = b[0]
	if id_a == id_b: #if the @id is the same, then the data sets are equivalent
		test = True
		print(id_a + ' and ' + id_b + ' are equivalent data sets.')
		y = 'equivalent'
	else: #if everything is the same except the @id, the data sets are equivalent
		x = [i for i, j in zip(a, b) if i == j]
		if len(x) == len(a) - 1:
			test = True
			print(id_a + ' and ' + id_b + ' are equivalent data sets.')
			y = 'equivalent'
		elif len(a[1]) != 0 and len(b[1]) != 0:
			r_id_a = a[1] #list of related identifiers for the two data sets being compared
			r_id_b = b[1]
			lra = len(r_id_a)
			lrb = len(r_id_b)
			if lra > lrb:
				for w in r_id_b:
					if w in r_id_a:
						test = True
						print(id_a + ' and ' + id_b + ' are related data sets.')
						y = 'related'
			elif lrb > lra:
				for w in r_id_a:
					if w in r_id_b:
						test = True
						print(id_a + ' and ' + id_b + ' are related data sets.')
						y = 'related'
			else:
				if r_id_a == r_id_b:
					test = True
					print(id_a + ' and ' + id_b + ' are related data sets.')
					y = 'related'
		else:
			xid_a = a[5] #compares doi, minid, and data guid
			xid_b = b[5]
			a_doi = xid_a['doi']
			b_doi = xid_b['doi']
			a_minid = xid_a['minid']
			b_minid = xid_b['minid']
			a_dataguid = xid_a['dataguid']
			b_dataguid = xid_b['dataguid']
			a_md5 = xid_a['md5']
			b_md5 = xid_b['md5']
			if a_dataguid == b_dataguid and a_minid == b_minid and a_doi == b_doi and a_md5 == b_md5:
				test = True
				print(id_a + ' and ' + id_b + ' are equivalent data sets.')
				y = 'equivalent'
			if a_dataguid != b_dataguid and a_minid == b_minid and a_doi != b_doi and a_md5 != b_md5:
				test = True
				print(id_a + ' and ' + id_b + ' are related data sets.')
				y = 'related'
	return(id_a,id_b,y,test)

#using the list of all key combinations, compare the values
#return a list of equivalent and related identifiers as tuples
equiv = []
for p,q in z:
	print(p)
	print(q)
	a = results[p]
	b = results[q]
	r,s,t,u = relat_test(a,b)
	if u == True:
		equiv.append((r,s,t))
print(equiv)
