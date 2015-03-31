spaces = [i for i in range(1,10)]

def print_ultimate_board(spaces):
	print "\n\nLet's play ULTIMATE tic-tac-toe! Choose the number of the space you'd like to occupy.\n\n"
	for a in range(9):
		for b in range(9):
			if (a*9+b) < 9:
				print str(spaces[a*9+b])+"____|",
			else:
				print str(spaces[a*9+b])+"___|",	
		print "\n"

def print_board(spaces):
	print "\n\nLet's play tic-tac-toe! Choose the number of the space you'd like to occupy.\n\n"
	for i in range(3):
		for j in range(3):
			print str(spaces[i*3+j])+"___|",
		print "\n"

def print_uboard(spaces):
	print "\n\nLet's play tic-tac-toe! Choose the number of the space you'd like to occupy.\n\n"
	for i in range (3):
		for x in range (3):
			for j in range (3):
				print str(spaces[i*3+j])+"___|" + str(spaces[i*3+j])+"___|" + str(spaces[i*3+j])+"___|",
			print "\n"
		
			
print print_uboard(spaces)
					