number = int(input("Enter number : "))

def printDivisors(number):
	L = []
	for i in range(1,int(number/4)+1):
		if number%i ==0:
			L.append(i)
			L.append(int(number/i))
	return L
A=printDivisors(number)
print(A)
