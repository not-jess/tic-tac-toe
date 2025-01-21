import random

theBoard = { 'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
	'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
	'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' ' }
# print(theBoard.items()
print("Welcome to tic-tac-toe mint")
print("Choose mode:")
print("1. vs Player")
print("2. vs CPU")

player1 = 'Player 1'
player2 = 'Player 2'
moves=0
while(True):
	if(moves==9):
		print("Draw")
		break
	if(moves%2==0):
		value='X'
		currPlayer=player1
	else:
		value='O'
		currPlayer=player2
	win=0
	while(True):
		print(currPlayer + ": ")
		move = input()
		if move not in theBoard.keys():
			print("Please input a valid spot")
			continue
		if(theBoard[move] != ' '):
			theBoard[move] != ' '
			print("Spot already taken")
			continue
		theBoard[move] = value
		try:
			x, y = move.split('-')
		except:
			print("Failed to split spot")
			continue
		for i in [x+'-L', x+'-M', x+'-R']:
			if(theBoard[i]==value):
				win += 1
			else:
				break
		if(win==3):
			break
		win=0
		for i in ['top-'+y, 'mid-'+y, 'low-'+y]:
			if(theBoard[i]==value):
				win += 1
			else:
				break
		if(win==3):
			break
		win=0
		moves += 1
		break
	if(win==3):
		print(currPlayer  + " wins!")
		break
