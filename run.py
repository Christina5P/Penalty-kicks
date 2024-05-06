import random

# List for direction you will kick  
kicks_direction = ['lt', 'lb', 'mt', 'mb', 'rt', 'rb', 'out']
lt = 'lefttop'
lb = 'leftbottom'
mt = 'middletop'
mb = 'middlebottom'
rt = 'righttop'
rb = 'rightbottom'
out = 'out'

# Enter name and ask for instruction or move to game
name = input('Hi Soccerplayer! Please enter your name: ')
response = input(f'Thanks {name}, Do you want to see instructions? (y/n): ')

if response.lower() == 'y':
    print('instructions') 
elif response.lower() == 'n':
    print("OK, we start!\n")
else:
    print('Something went wrong, please answer (y/n):')

"""
function for player to kick to any of 6 direction, player has choosen from.
The goalkeeper will either stay in center or jump to left or right side
to catch the ball.
"""

def penaltyAgainst():

    # players choice of direction:
    
    print ('Choose spot from:\n lt=Left Top,\n lb=Left bottom,\n mt=Middle Top\n mb=Middle Bottom\n rt=Right Top\n rb=Right bottom')
    userOption = input('Pick your spot:')   

    # randomchoice for the goalkeeper:
    goalkeeper = random.choice(kicks_direction)
    print('Goalkeeper dives to', goalkeeper)

    if goalkeeper == userOption:
         print('Goalkeeper catched the ball!')
    else:
         print ('GOAL!')

# call for the function
penaltyAgainst()

""" 
totalPenalties=0
userscore = 0
computerscore = 0

# Count goals from player and computer up to 6 shoots
while totalPenalties < 6:
    penaltyFor ()
    penaltyAgainst()
    penaltyScores()
    finalScore()    
""" 