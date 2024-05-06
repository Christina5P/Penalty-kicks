import random

kicksdirection = ['lt', 'lb', 'mt', 'mb', 'rt', 'rb']
lt = 'lefttop'
lb = 'leftbottom'
mt = 'middletop'
mb = 'middlebottom'
rt = 'righttop'
rb = 'rightbottom'

# Enter name and ask for instruction or move to game
name = input('Hi Soccerplayer! Please enter your name: ')
response = input(f'Thanks {name}, Do you want to see instructions? (y/n): ')

if response.lower() == 'y':
    print('instructions') 
elif response.lower() == 'n':
    print ("OK, click enter and let's start")
else:
    print ('Something went wrong, please answer (y/n):')





totalPenalties=0
userscore = 0
computerscore = 0

# Count goals from player and computer up to 6 shoots
while totalPenalties < 6:
    penaltyFor ()
    penaltyAgainst()
    penaltyScores()
finalScore()    
