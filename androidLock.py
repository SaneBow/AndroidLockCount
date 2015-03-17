"""Count the number of possible Android Screen Lock patterns"""
from itertools import permutations as p 

sum=0

def valid(ptuple):
	"""Check if a permutation is valid (e.g. 1234->True, 1239->False)"""
	nstr = ''.join([str(i) for i in ptuple])
	checkDict = {'2':('13','31'),'4':('17','71'),'6':('39','93'),'8':('79','97'),'5':('19','91','28','82','37','73','46','64')}
	for k,vt in checkDict.items():
		for v in vt:
			pos = nstr.find(v)
			if pos >= 0 and k not in nstr[:pos]:
				return False
	return True

for n in xrange(4,10):
	sum += len([t for t in p(xrange(1,10),n) if valid(t)])

print "There are",sum,"possible patterns in total."