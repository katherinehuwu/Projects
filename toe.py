spaces = [i for i in range(1, 10)]

def print_board(spaces):
	print "\n\nLet's play tic-tac-toe! Choose the number of the space you'd like to occupy.\n\n"
	for i in range(3):
		for j in range(3):
			print str(spaces[i*3+j])+"___|",
		print "\n"

def prompt():
	total = 1
	while total == 1:
		ask = raw_input("\n\nDo you want to play Tic-Tac Toe? Enter Y or N: \n\n")	
		if ask == "Y":
			print play(1, choice)
		elif ask == "N":
			print "\n\nAh well, maybe next time then! Bye bye.\n\n"
			total += 2
		else:
			ask = raw_input("\n\nThat wasn't Y or N. Press any key and I'll give you another chance. \n\n")
			total = 1
	else: 
		exit()

win = [[1,2,3], [1,5,9], [1,4,7], [4,5,6], [3,5,7], [7,8,9], [2,5,8], [3,6,9]]
turn = True
mark= ""
choice = ""
userx = []
usero = []
user = []

def play(turn, choice):			
	if turn == 1:
		mark = "X"
		user = userx
	else:
		mark = "O"
		user = usero
	print_board(spaces)
	print "It's User %s turn now." %(mark) 
	choice = raw_input("\n\nHi User %s ! Enter the number you want to occupy: \n\n"%(mark)) 
	while choice.isdigit() == False or int(choice) not in spaces:
		choice =  raw_input("\n\nPlease enter a valid number on the board. Try again: \n\n ")  
	else: 
		choice = int(choice)
		spaces[choice-1] = mark
	while len(user) <= 5: 
		user.append(choice)
		for sets in win:
			if set(sets) & set(user) == set(sets):
				print_board(spaces)
				print "Congrats User %s !You won!" %(mark), prompt()
		if len(user)> 4:
			print "It's a tie!", prompt()
		else:
			print play(turn*(-1), "%s"%(mark))

print prompt()
