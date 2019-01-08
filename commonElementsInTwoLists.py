L = [1,1,2,3,5,8,13,21,34,55,89]
L2 = [1,2,3,4,5,6,7,8,9,10,11,12,13]
def commonElements(L,L2):
	L1 = []
	for x in set(L):
		if x in set(L2):
				L1.append(x)
	return L1
L = commonElements(L,L2)
print(L)


	
	