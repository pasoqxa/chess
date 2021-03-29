import os

os.system('cls')
gamesdir = 'c:/users/tieri/desktop/chessbo/'

os.chdir(gamesdir) # current directory with games in cmd
dir = os.listdir()


count = 0
dirlist = []
for line in dir: 
	print(line)
	count += 1
	dirlist.append(line) #lists with names of games  
dicts = dict(list(enumerate(dirlist))) #dictionary with 

a = int(input('\nEnter a number of game you would like to analyse \n\n'))

def choosing(a): 
	if type(a) is int and a >= 0 and a <= count:
		dicts.get(a)
		os.system('start '+ gamesdir + dicts.get(a-1))
	else:
		os.system('cls')
		print('Try again')
		a = int(input('Enter a number of game you would like to analyse \n'))
		return choosing(a)

choosing(a) #opens a game