import random  # randomchoice to goalkeeper
from colorama import Fore, Back, Style  # colour to text
import pyfiglet  # for design text
import os  # clear terminal
from google.oauth2.service_account import Credentials  # api
from googleapiclient.discovery import build
import sys  # for typing instructions
import time  # for typing instructions


SCOPES = ['https://www.googleapis.com/auth/documents.readonly']
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPES)
DOC_SERVICE = build('docs', 'v1', credentials=SCOPED_CREDS)

DOCUMENT_ID = 'https://docs.google.com/document/d/1fJO5gAoMi7rKUywXLD60dA-wM5b8s5z6QXKmCr07rmc/edit?usp=sharing'
document_id = DOCUMENT_ID.split('/')[5]

kicks_direction = ['lt', 'lb', 'mt', 'mb', 'rt', 'rb']
"""
create direction from array in a dictionary, så you can text short names
but look at full name for better understanding
"""

directions = {'lt': 'Left Top',
              'mt': 'Middle Top',
              'rt': 'Right top',
              'lb': 'Left Bottom',
              'mb': 'Middle Bottom',
              'rb': 'Right bottom'}


# Welcome to Penalty Kick banner

def print_welcome_banner():
    welcome_banner = pyfiglet.figlet_format('Welcome to\nPenalty kick')
    print(welcome_banner)


def print_instructions(instructions):
    """typing instruction from API
    """
    for char in instructions:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print()


def main():
    """function start with asking for name
    and if you want to see the instructions from api
    """
    print_welcome_banner()
    document = DOC_SERVICE.documents().get(documentId=document_id).execute()
    instructions = ''
    for element in document.get('body', {}).get('content', []):
        if 'paragraph' in element:
            for run in element['paragraph']['elements']:
                if 'textRun' in run:
                    instructions += run['textRun']['content']

    while True:
        name = input('Hi Soccerplayer! Please enter your name: ')
        response = input(f'Thanks {name},\n Do you want to see instructions?\
         (y/n):')

        if response.lower() == 'y':
            print_instructions(instructions)
            break
            os.system('cls' if os.name == 'nt' else 'clear')

        elif response.lower() == 'n':
            print("\nOK, we start!\n")
            break
        else:
            print('Something went wrong, please answer (y/n):')
            continue
        os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == "__main__":
    main()


def penalty():
    """
    Function and algorithm for the game. Start with players choice of direction
    and compares to goalkeepers random. There is up to 6 penalties if you don't
    win before.
    """
    total_penalties = 0
    goalkeeper_scores = 0
    penalty_scores = 0

    while total_penalties < 6:
        print('''Choose spot from:
lt=Left Top, mt=Middle Top, rt=Right Top,
lb=Left bottom, mb=Middle Bottom, rb=Right bottom''')
        user_option = input('\nWhere would you like to shoot?:\n')
        valid_options = ['lt', 'mt', 'rt', 'lb', 'mb', 'rb']
        os.system('cls' if os.name == 'nt' else 'clear')
        if user_option in valid_options:
            print(Back.WHITE + Fore.BLACK + f'You chose:\
                 {directions[user_option]:<10}' + Style.RESET_ALL)
            goalkeeper_group = get_goalkeeper_choice()
            print(Back.WHITE + Fore.BLACK + 'Goalkeeper dives to: '
                  f"{directions[goalkeeper_group[0]]:<20} \
                    ,{directions[goalkeeper_group[1]]:<5}",
                  Style.RESET_ALL)

            if user_option in goalkeeper_group:
                result = pyfiglet.figlet_format('Goalkeeper caught!')
                print(Fore.RED + result + Style.RESET_ALL)
                goalkeeper_scores += 1
            elif user_option not in goalkeeper_group:
                result = pyfiglet.figlet_format('GOOAAL!')
                print(Fore.GREEN + result + Style.RESET_ALL)
                penalty_scores += 1

            total_penalties += 1
        else:
            print(Fore.RED + Back.WHITE + '\nYou stumbled on the keys,\
                 Please choose from lt, lb, mt, mb, rt, rb\n\
                    ' + Style.RESET_ALL)
        print(Back.CYAN + Fore.BLACK + f'Total penalties taken:\
             {total_penalties:< 15}' + Style.RESET_ALL)
        print(Back.CYAN + Fore.BLACK + f'Score: Player {penalty_scores:>5} \
            - Goalkeeper {goalkeeper_scores:>5}' + Style.RESET_ALL)

        if penalty_scores > 3:
            print('\nYou won!!!')
            break

        elif goalkeeper_scores > 3:
            print('You lost.')
            break

        elif penalty_scores == 3 and goalkeeper_scores == 3:
            print('It ended in a draw. You get a new round again')
            break


def get_goalkeeper_choice():
    groups = [['lt', 'lb'], ['mt', 'mb'], ['rt', 'rb']]
    return random.choice(groups)


# Call function for game
penalty()


# restart or exit
def restart_game():
    while True:
        response = input('\nGood job! Do you want to restart? y/n: ')
        if response.lower() == 'y':
            print('')
            print('Start a new game\n')
            os.system('cls' if os.name == 'nt' else 'clear')
            penalty()
        elif response.lower() == 'n':
            print("\nOK, see you next time \n")
            break

        else:
            print('Something went wrong, please answer (y/n):')


# Call restart_game function
restart_game()
