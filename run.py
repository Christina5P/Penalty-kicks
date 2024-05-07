import matplotlib.pyplot as plt # soccer pitch
from mplsoccer import Pitch, VerticalPitch
import random # randomchoice to goalkeeper
import json 
from colorama import Fore, Back, Style #colour to text

pitch = VerticalPitch(half=True)
pitch = Pitch(pitch_color='grass', line_color='white',
              stripe=True) 
fig, ax = pitch.draw()

# List for direction you will kick  
kicks_direction = ['lt', 'lb', 'mt', 'mb', 'rt', 'rb']
# dictionary of directions
directions = {'lt': 'Left Top',
    'lb': 'Left Bottom',
    'mt': 'Middle Top',
    'mb': 'Middle Bottom',
    'rt': 'Right top',
    'rb': 'Right bottom',
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
# variabel
total_penalties = 0   # totalPenalties = penalty(totalPenalties) # antalet sparkar
goalkeeper = None

""" 
print('         _____________________________________       ')
print('          /                                  \        ')
print('         /                                    \       ')
print('        /                                      \      ')
print('       /                                        \      ')
print('      /                                          \     ')
print('     /                                            \    ') 
print('   ------------------------------------------------   ')   
print('')
print('')
""" 
def penalty():
    global total_penalties
    penalty_Scores = 0
    goalkeeper_Scores = 0

    while total_penalties < 10:
        # players choice of direction:
        print('Choose spot from:\n lt=Left Top   lb=Left bottom,\n mt=Middle Top mb=Middle Bottom\n rt=Right Top  rb=Right bottom')
        userOption = input('Where would you like to shoot?:   ')   

        # randomchoice for the goalkeeper:
        goalkeeper = random.choice(kicks_direction)
        print('')
        print('Goalkeeper dives to:', directions[goalkeeper])

        if goalkeeper == userOption:
            print(Fore.RED + 'Goalkeeper catched the ball!')
            print('')
            goalkeeper_Scores += 1
        elif goalkeeper != userOption:
            print(Fore.GREEN + 'GOOAAL!')
            penalty_Scores += 1
            print('')
        else:
            print(Fore.RED + 'Try again!')
            
        total_penalties += 1

    if total_penalties == 6:
        # Describe how many penalties are used
        print(f'Total penalties taken: {total_penalties}')
        print(f'Final score: Player {penalty_Scores} - Goalkeeper {goalkeeper_Scores}')
        return

penalty()
