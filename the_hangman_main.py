'''
The Hangman Game's main menu
'''
import time
from the_hangman_files.the_hangman_app_core import app_core
from the_hangman_files.the_hangman_global_f import clear, show_game_title, \
    show_welcome, load_game_records, show_game_records, main_menu

def main():
    clear()
    show_game_title()
    print('\n')
    show_welcome()
    input('\n\n\tPress ENTER to continue...')
    records = load_game_records()
    PLAY, RECORDS, EXIT = '1', '2', '0'
    menu = True
    while menu:
        clear()
        show_game_title()
        print('\n')
        main_menu()
        opt = input('\n\t\t     >> SELECT: ').strip()
        if opt == PLAY:
            records = app_core(records)
        elif opt == RECORDS:
            clear()
            show_game_title()
            print('\n')
            show_game_records(records)
        elif opt == EXIT:
            clear()
            show_game_title()
            print('\n\n\t    >> THANKS FOR PLAYING!!! <<')
            time.sleep(4)
            menu = False
        else:
            print('\n\t\t   Invalid option!!!')
            time.sleep(1.5)