string = input("Enter the String : ")
L = len(string)
flag = True
for i in range(0,int(L/2)):
	if string[i] != string[L-i-1]:
		flag = Flase;
if flag ==True:
	print(string+" is palindrome.")
else :
	print(string+" is not palindrome.")
