'''
Set of functions to use in The Hangman Game
'''
import os, json, time

def clear():
    ''' clear screen function '''
    if os.name == 'posix':   # linux and mac
        os.system('clear')
    else:                    # windows = 'nt'
        os.system('cls')

def main_menu():
    options = ('play', 'records')
    print('\t\t-###   MAIN MENU   ###-\n')
    for i, option in enumerate(options):
        print(f'\t\t     ({i + 1}) {option.upper()}')
    print('\t\t     (0) EXIT APP')

def load_game_files():
    try:
        all_words = list()
        filename = 'the_hangman_data/the_hangman_words.txt'
        with open(filename, 'r') as file_obj:
            for line in file_obj:
                all_words.append(line.strip())
        all_words = tuple(all_words)
        filename = 'the_hangman_data/the_hangman_graphics.json'
        with open(filename, 'r') as file_obj:
            life_graphics = json.load(file_obj)
    except FileNotFoundError:
        clear()
        show_game_title()
        print('\n\n\tThe files the_hangman_words.txt and\n'
            '\tthe_hangman_graphics.json,\n'
            '\tMUST BE inside the_hang_man_data folder')
        input('\n\n\tPress ENTER to close application...')
        exit()
    else:
        return all_words, life_graphics

def load_game_records():
    try:
        filename = 'the_hangman_data/the_hangman_records.json'
        with open(filename, 'r') as file_obj:
            records = json.load(file_obj)
    except FileNotFoundError:
        records = []
    
    return records

def show_game_records(records:list):
    if len(records) > 0:
        longest_name = ''
        for name in records[::2]:
            if len(name) > len(longest_name):
                longest_name = name
        esp = (len(longest_name) + 3)
        if len(longest_name) < 7:
            esp = 10
        print(f'\t### |RECORDS| {"#"*(esp - 2)}\n')
        print(f'\t    PLAYER{" "*(esp - 5)}ROUNDS\n')
        count = 1
        for i in range(0, len(records), 2):
            if count == 10:
                print(f'\t{count}.- {records[i].upper()} '
                    f'{"-"*(esp - len(records[i]))} {records[i + 1]}')
            else:
                print(f'\t {count}.- {records[i].upper()} '
                    f'{"-"*(esp - len(records[i]))} {records[i + 1]}')
            count += 1
    else:
        print("\n\tNo records yet!! Let's play!!...")
    input('\n\n\n\tPres ENTER to GO BACK...')

def show_game_title():
    title = '| · - ·     T H E   H A N G M A N   G A M E     · - · |'
    print(f"{'-'*len(title)}\n{title}\n{'-'*len(title)}")

def show_welcome():
    print('\tWelcome to The Hangman Game!!!\n'
        '\tMore than 1500 words are waiting to you!!!'
        '\n\tFind the word behind "#" before lifes get 0\n'
        '\tWords will turn harder round after round')

def set_player_name():
    player_name = input('\t>> Type your NAME: ').strip()
    if len(player_name) == 0 or len(player_name) > 25:
        print('\n\tInvalid NAME!!! Type again!!! (MAX lenght: 25)')
        time.sleep(2)
        return 0
    else:
        return player_name

def show_start_banner(player_name:str):
    counter = 3
    for i in range(4):
        clear()
        show_game_title()
        print(f'\n\n\t\tOK, {player_name.upper()}')
        if i == 3:
            print('\n\t\t    GO!!!')
            time.sleep(1.5)
        else:
            print(f'\n\t\tStarting in {counter}...')
            counter -= 1
            time.sleep(1)