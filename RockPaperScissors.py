print("***Enter names of the players***")
P1 = input("Player 1 name : ")
P2 = input("Player 2 name : ")

new = "y"											
while(new== "y"):
	print("Input \n1 for Rock \n2 for Paper\n3 for Scissors")
	print(P1+"'s turn")
	choiceP1 = int(input(P1+"'s inupt : "))
	print(P2+"'s turn")
	choiceP2 = int(input(P2+"'s input : "))
	if(choiceP1==choiceP2):
		print("It's a Tie")
	elif(choiceP1==1 and choiceP2==3):
		print("Congo "+P1)
	elif(choiceP1==3 and choiceP2==1):
		print("Congo "+P2)
	elif(choiceP1==2 and choiceP2==1):
		print("Congo "+P1)
	elif(choiceP1==1 and choiceP2==2):
		print("Congo "+P2)
	elif(choiceP1==2 and choiceP2==3):
		print("Congo "+P2)
	elif(choiceP1==3 and choiceP2==2):
		print("Congo "+P1)
	print("\nWant to play new game ")
	new=input("y / n : ")

