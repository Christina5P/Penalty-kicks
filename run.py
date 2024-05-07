import matplotlib.pyplot as plt  # soccer pitch
from mplsoccer import Pitch, VerticalPitch

import random  # randomchoice to goalkeeper
from colorama import Fore, Back, Style  #colour to text

# to animate soccerpitch
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
    # error msg:
else:
    print('Something went wrong, please answer (y/n):')

"""
function for player to kick to any of 6 direction, player has choosen from.
The goalkeeper will either stay in center or jump to left or right side
to catch the ball.
"""


# variabel totalPenalties,  penalty(totalPenalties) counts shoots 
total_penalties = 0 
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

# function for player to choose where to shoot
def penalty():
    global total_penalties, goalkeeper
    penalty_scores = 0
    goalkeeper_scores = 0

    while total_penalties < 6:
        print('Choose spot from:\n lt=Left Top   lb=Left bottom,\n mt=Middle Top mb=Middle Bottom\n rt=Right Top  rb=Right bottom')
        print('')
        user_option = input('Where would you like to shoot?:  ')  
        print('') 
        valid_options = ['lt', 'lb', 'mt', 'mb', 'rt', 'rb']
        
        if user_option in valid_options:
            print(f'You chose: {user_option}')
            goalkeeper = random.choice(kicks_direction)
            print('')
            print('Goalkeeper dives to:', directions[goalkeeper])
            penalty_scores += 1
            
            if goalkeeper == user_option:
                print(Fore.RED + 'Goalkeeper catched the ball!' + Style.RESET_ALL)
                print('')
                goalkeeper_scores += 1
            else:
                print(Fore.GREEN + 'GOOAAL!' + Style.RESET_ALL)
                penalty_scores += 1
                print('')
        else:
            print(Fore.RED + 'Invalid option! Please choose from lt, lb, mt, mb, rt, rb.' + Style.RESET_ALL)
            print('')
            
        total_penalties += 1

    if total_penalties <= 6:
        print(f'Total penalties taken: {total_penalties}')
        print(f'Final score: Player {penalty_scores} - Goalkeeper {goalkeeper_scores}')

# Call function
penalty()
# restart or exit 

restart= input('Good job! Do you want to restart? y/n:  ')
if response.lower() == 'y':
    print('Start a new game') 
    RESET_ALL

elif response.lower() == 'n':
    print("OK, see you next time \n")
    exit

    # error msg:
else:
    print('Something went wrong, please answer (y/n):')
