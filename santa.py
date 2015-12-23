import random
pairs = []
peeps = {1:"Bryan", 2: "Will", 3: "Lee", 4: "Eric", 5: "Michelle", 6: "Vincent", 7: "Brooke", 8: "Janu"}
peepSet = set(range(1,9))
def samp():
	return random.sample(peepSet, 1)[0]

for p in peeps.keys():
#	print p
#	print pairs
	pair = 0
	if p == 2:
		pair = 1
	elif p == 4:
		while pair in [0,5]:
			pair = samp()
	elif p == 5:
		while pair in [0,4]:
			pair = samp()
	elif p == 6:
		while pair in [0,7]:
			pair = samp()
	elif p == 7:
		while pair in [0,6]:
			pair = samp()
	else: 
		while pair in [0,p]:
			pair = samp()
	 
	pairs.append( (peeps[p], peeps[pair]))
	peepSet.remove(pair)

print pairs