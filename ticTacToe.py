import random

theBoard = { 'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ',
	'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ',
	'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' ' }

enableShowBoard = True

def showBoard():
	global enableShowBoard
	if(enableShowBoard == False):
		return
	print(theBoard['top-L'] + ' | ' + theBoard['top-M'] + ' | ' + theBoard['top-R'])
	print('---------')
	print(theBoard['mid-L'] + ' | ' + theBoard['mid-M'] + ' | ' + theBoard['mid-R'])
	print('---------')
	print(theBoard['low-L'] + ' | ' + theBoard['low-M'] + ' | ' + theBoard['low-R'])

def toggleBoard():
	global enableShowBoard
	if(enableShowBoard == False):
		enableShowBoard = True
	else:
		enableShowBoard = False

def clearBoard():
	global theBoard
	theBoard = theBoard.fromkeys(theBoard.keys(), ' ')

def main():
	while(True):
		print("Welcome to tic-tac-toe mint")
		print("1. Play a game")
		print("2. Settings")
		print("3. Exit")
		print(">> ", end='')
		choice = int(input())
		if(choice == 1):
			playMenu()
		elif(choice == 2):
			settingsMenu()
		elif(choice == 3):
			break
		else:
			print("Please input a valid choice!")

def playMenu():
	while(True):
		print("Choose mode:")
		print("1. Vs Player")
		print("2. Vs CPU")
		print("3. Back")
		print(">> ", end='')
		choice = int(input())
		if(choice == 1):
			playPlayer()
		elif(choice == 2):
			playCPU()
		elif(choice == 3):
			break
		else:
			print("Please input a valid choice!")

def settingsMenu():
	while(True):
		print("1. Show board after each moves: " + str(enableShowBoard))
		print("2. Back")
		print(">> ", end='')
		choice = int(input())
		if(choice == 1):
			toggleBoard()
		elif(choice == 2):
			break
		else:
			print("Please input a valid choice!")


def playPlayer():
	play()

def playCPU():
	play(True)


def play(vsCpu = False):
	clearBoard()
	if(vsCpu == True):
		if(random.randint(0,1)==0):
			player1 = 'Player'
			player2 = 'CPU'
		else:
			player1 = 'CPU'
			player2 = 'Player'
	else:
		player1 = 'Player 1'
		player2 = 'Player 2'
	moves=0

	while(True):
		showBoard()
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
			print(currPlayer + ": ", end='')

			if(vsCpu == True and currPlayer == 'CPU'):
				move = random.choice(list(theBoard.keys()))
				print(move)
			else:
				try:
					move = input()
				except KeyboardInterrupt:
					return

			if move not in theBoard.keys():
				print("Please input a valid spot (top-L, mid-M, low-R, etc)")
				continue
			
			if(theBoard[move] != ' '):
				theBoard[move] != ' '
				print("Spot already taken")
				continue

			moves += 1
			theBoard[move] = value
			x, y = move.split('-')

			for i in [x+'-L', x+'-M', x+'-R']:
				if(theBoard[i]==value):
					win += 1
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
			break
		if(win==3):
			showBoard()
			print(currPlayer  + " wins!")
			break

if __name__ == '__main__':
    main()