import random

# List for direction you will kick  
kicks_direction = ['lt', 'lb', 'mt', 'mb', 'rt', 'rb', 'out']
# dictionary of directions
directions = {  'lt': 'lefttop',
    'lb': 'leftbottom',
    'mt': 'middletop',
    'mb': 'middlebottom',
    'rt': 'righttop',
    'rb': 'rightbottom',
    'out': 'out'
}


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

# function for players penaltys agains goalkeepers choice

total_penalties = 0   # totalPenalties = penalty(totalPenalties) # antalet sparkar

def penalty():
    global total_penalties
 
    # new tries from player and computer up to 6 shoots
    while total_penalties < 10:
        total_penalties += 1

    # players choice of direction:
print ('Choose spot from:\n lt=Left Top   lb=Left bottom,\n mt=Middle Top mb=Middle Bottom\n rt=Right Top  rb=Right bottom')
userOption = input('Where would you like to shoot?:   ')   

    # randomchoice for the goalkeeper:
goalkeeper = random.choice(kicks_direction)
print('')
print('Goalkeeper dives to:', directions[goalkeeper])


if goalkeeper == userOption:
         print('Goalkeeper catched the ball!')
elif goalkeeper!= userOption:
         print ('GOOAAL!')  
else:
        print ('Try again!')    
print('')  




print('         ______________________________________       ')
print('         /                                   \        ')
print('        /                                     \       ')
if goalkeeper!= userOption:
    print('       /        W                               \      ')
else:   
    print('       /                                    \      ')
print('      /                                         \     ')
print('     /                                           \    ') 
print('   ------------------------------------------------   ')   
print('')
print('')


print('Choose again, next penalty:') 
userOption = input() 
  
# Describe how many penalties are used
print(f'Total penalties taken: {total_penalties}')

penalty_Scores = 0
goalkeeper_Scores = 0
print(f'Final score: Player {penalty_Scores} - Goalkeeper {goalkeeper_Scores} ')

