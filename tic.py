spaces = []
for i in range(1,10):
	spaces.append(i) 

def print_board(spaces):
	print "To play this game, choose the number of the space you'd like to occupy.\n"
	for i in range(3):
		for j in range(3):
			print str(spaces[i*3+j])+"___|",
		print "\n"

win = [[1,2,3], [1,5,9], [1,4,7], [4,5,6], [3,5,7], [7,8,9], [2,5,8], [3,6,9]]
xchoice = 0
ochoice = 0
userx = []
usero = []

def xturn(xchoice):		
	turns = True
	xchoice = raw_input("Hi User X! Enter the number you want to occupy: ")
	while xchoice.isdigit() == False or int(xchoice) not in spaces:
		xchoice = raw_input("Please enter a valid number on the board. Try again: ")  
	else: 
		xchoice = int(xchoice)
	while turns is True:
		spaces[xchoice-1] = "X"
		userx.append(xchoice)
		if len(userx) < 3:
			turns = False
		elif len(userx) == 3:
			if sorted(userx) in win:
				print print_board(spaces), "Congrats! You won :) "
				exit()
			else:
				turns = False
		else: 
			for sets in win:
				if set(sets) & set(userx) == set(sets):
					print print_board(spaces), "Congrats! You won :) "
					exit()
				elif len(userx) < 5:
					turns = False	
				else:
					print print_board(spaces), "It's a tie!Play again"
					exit()	
	else:
		print print_board(spaces), "It's User O's turn now."
		print oturn(ochoice)
#Weird loop problem with userX"Enter a number on the board. Try again")
def oturn(ochoice):
	turns = False
	ochoice = raw_input("Hi User O! Enter the number you want to occupy: ")
	while ochoice.isdigit() == False or int(ochoice) not in spaces:
		ochoice = raw_input("Please enter a valid number on the board. Try again: ")  
	else:
		ochoice = int(ochoice)
	while turns is False:
		spaces[ochoice-1] = "O"
		usero.append(ochoice)
		if len(usero) < 3:
			turns = True
		elif len(usero) == 3:
			if sorted(usero) in win:
				print print_board(spaces), "Congrats! You won :) "
				exit()
			else:
				turns = True
		else: 
			for sets in win:
				if set(sets) & set(usero) == set(sets):
					print print_board(spaces), "Congrats! You won :) "
					exit()
				else:
					turns = True		
	else:
		print print_board(spaces), "It's User X's turn now."
		print xturn(xchoice)

print print_board(spaces)
print xturn(xchoice)

		
