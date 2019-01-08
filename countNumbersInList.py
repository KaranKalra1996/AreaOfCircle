L = [1,1,2,3,5,8,13,21,34,55,89]
A = []
count = 0
for i in L:
	if i < 5:
		count = count +1
		print(i)
print("Number of elements less than 5 in list L are : "+str(count))
num = int(input("Enter number : "))
for i in L:
	if i < num:
		A.append(i)
print(A)

