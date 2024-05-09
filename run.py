import random  # randomchoice to goalkeeper
from colorama import Fore, Back, Style  # colour to text
from pyfiglet import Figlet

import matplotlib.pyplot as plt
from mplsoccer import Pitch, VerticalPitch

# animate soccerpitch
pitch = VerticalPitch(half=True)
pitch = Pitch(pitch_color='grass', line_color='white',stripe=True) 
fig, ax = pitch.draw()

                                  
# List for direction you will kick  
kicks_direction = ['lt', 'lb', 'mt', 'mb', 'rt', 'rb']
# dictionary of directions
directions = {'lt': 'Left Top',
              'lb': 'Left Bottom',
              'mt': 'Middle Top',
              'mb': 'Middle Bottom',
              'rt': 'Right top',
              'rb': 'Right bottom'}
 
# Welcome to Penalty Kick 

# Enter name and ask for instruction or move to game


name = input('Hi Soccerplayer! Please enter your name: ')

while True:
    response = input(f'Thanks {name}, Do you want to see instructions? (y/n): ')

    if response.lower() == 'y':
        print('instructions') 
        print('')
        break
    elif response.lower() == 'n':
        print('')
        print("OK, we start!\n")
        break            

        # error msg:
    else:
        print('Something went wrong, please answer (y/n):')
     

# variabel totalPenalties,  penalty(totalPenalties) counts shoots 
total_penalties = 0 
goalkeeper_scores = 0
penalty_scores = 0

# function for player to choose where to shoot
def penalty():
    global total_penalties, penalty_scores, goalkeeper_scores
    total_penalties = 0
    while total_penalties < 6:
        print('Choose spot from:\n lt=Left Top   lb=Left bottom,\n mt=Middle Top mb=Middle Bottom\n rt=Right Top  rb=Right bottom')
        print('')
        user_option = input('Where would you like to shoot?:  ')  
        print('') 
        valid_options = ['lt', 'lb', 'mt', 'mb', 'rt', 'rb']
        
        if user_option in valid_options:
            print(Back.WHITE + Fore.BLACK + f'You chose:', directions [user_option] + Style.RESET_ALL)
            goalkeeper = random.choice(kicks_direction)
            print('')
            print(Back.WHITE + Fore.BLACK + 'Goalkeeper dives to:', directions[goalkeeper] + Style.RESET_ALL)
                
            if goalkeeper == user_option:
                print('')
                print(Fore.RED + 'Goalkeeper catched!' + Style.RESET_ALL)
                print('')
                goalkeeper_scores += 1
                total_penalties += 1
                
            elif user_option != goalkeeper:
                print(Fore.GREEN + 'GOOAAL!' + Style.RESET_ALL)
                penalty_scores += 1
                total_penalties += 1
                print('')
            
        else:
            print(Fore.RED + Back.WHITE + 'You stumbled on the keys, Please choose from lt, lb, mt, mb, rt, rb' + Style.RESET_ALL)
            print('')
                
        print(Fore.BLUE + f'                                       Total penalties taken: {total_penalties}' + Style.RESET_ALL)
        print(Fore.BLUE + f'                                       Score: Player {penalty_scores} - Goalkeeper {goalkeeper_scores}' + Style.RESET_ALL)
    
        if total_penalties >= 1:
            print(Back.WHITE + Fore.BLUE + f'Total penalties taken: {total_penalties}' + Style.RESET_ALL)
            print(Back.WHITE + Fore.BLUE + f'Score: Player {penalty_scores} - Goalkeeper {goalkeeper_scores}' + Style.RESET_ALL)
        

while True:    
    if penalty_scores > 3:
        print('You won!!!')
        break

    elif goalkeeper_scores > 3: 
        print('You lost.')
        break

    else:
        print('It ended in a draw. You get a new round again')
        break

# Call function for game
penalty()

# restart or exit 
print('')
while True:
        response=input('Good job! Do you want to restart? y/n: ')
        
        if response.lower() == 'y':
            print('')
            print('Start a new game')
            print('')
            penalty() 
            
        elif response.lower() == 'n':
            print('')
            print("OK, see you next time \n")
            break

        else:  
            print('Something went wrong, please answer (y/n):')
 
