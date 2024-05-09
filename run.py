import random  # randomchoice to goalkeeper
from colorama import Fore, Back, Style  # colour to text
import pyfiglet 
import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build    

SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)
DOC_SERVICE = build('docs', 'v1', credentials=SCOPED_CREDS)

DOCUMENT_ID = 'https://docs.google.com/document/d/1fJO5gAoMi7rKUywXLD60dA-wM5b8s5z6QXKmCr07rmc/edit?usp=sharing'
document_id = DOCUMENT_ID.split('/')[5]





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

def main():
    document = DOC_SERVICE.documents().get(documentId=document_id).execute()
    instructions = ""

    for element in document.get('body', {}).get('content', []):
        if 'paragraph' in element:
            for run in element['paragraph']['elements']:
                if 'textRun' in run:
                    instructions += run['textRun']['content']

    name = input('Hi Soccerplayer! Please enter your name: ')
    response = input(f'Thanks {name}, Do you want to see instructions? (y/n):')

    if response.lower() == 'y':
        print(instructions)
    elif response.lower() == 'n':
        print("\nOK, we start!\n")
    else:
        print('Something went wrong, please answer (y/n):')
if __name__ == "__main__":        
    main()

#os.system('cls' if os.name == 'nt' else 'clear')
        
# function for player to choose where to shoot
def  penalty():
     total_penalties = 0
     goalkeeper_scores = 0
     penalty_scores = 0
    
     while total_penalties < 6:
            print('Choose spot from:\n lt=Left Top   lb=Left bottom,\n mt=Middle Top mb=Middle Bottom\n rt=Right Top  rb=Right bottom')
            print('')
            user_option = input('Where would you like to shoot?:')  
            print('') 
            valid_options = ['lt', 'lb', 'mt', 'mb', 'rt', 'rb']
            os.system('cls' if os.name == 'nt' else 'clear')
            
            if user_option in valid_options:
                print(Back.WHITE + Fore.BLACK + f'You chose:', directions [user_option] + Style.RESET_ALL)
                goalkeeper = random.choice(kicks_direction)
                print('')
                print(Back.WHITE + Fore.BLACK + 'Goalkeeper dives to:', directions[goalkeeper] + Style.RESET_ALL)
                        
                if goalkeeper == user_option:
                    print('')
                    result = pyfiglet.figlet_format('Goalkeeper catched!') 
                    print(Fore.RED + result + Style.RESET_ALL)
                    print('')
                    goalkeeper_scores += 1
                    total_penalties += 1
                    
                elif user_option != goalkeeper:
                    print('')
                    result = pyfiglet.figlet_format('GOOAAL!') 
                    print(Fore.GREEN + result + Style.RESET_ALL)
                    penalty_scores += 1
                    total_penalties += 1
                    print('')
                
            else:
                print(Fore.RED + Back.WHITE + 'You stumbled on the keys, Please choose from lt, lb, mt, mb, rt, rb' + Style.RESET_ALL)
                print('')
            
            if total_penalties >= 1:
                print(Back.CYAN + Fore.BLACK + f'Total penalties taken: {total_penalties}' + Style.RESET_ALL)
                print(Back.CYAN + Fore.BLACK + f'Score: Player {penalty_scores} - Goalkeeper {goalkeeper_scores}' + Style.RESET_ALL)
                print('')
            if penalty_scores > 3:
                print('You won!!!')
                break

            elif goalkeeper_scores > 3:
                print('You lost.')
                break

            elif penalty_scores == 3 and goalkeeper_scores == 3:
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
 
