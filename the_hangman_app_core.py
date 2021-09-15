'''
Logic core of The Hangman Game
'''
import time
from the_hangman_files.the_hangman_classes import Game
from the_hangman_files.the_hangman_global_f import clear, show_game_title, \
    show_start_banner, set_player_name, load_game_files

def app_core(records:list):
    WORDS_DATABASE, LIFE_GRAPHICS = load_game_files()
    start_game = ask_player_name = retry = True
    while start_game:
        clear()
        show_game_title()
        print('\n')
        if ask_player_name:
            player_name = set_player_name()
            if player_name == 0:
                continue
        game = Game(player_name, LIFE_GRAPHICS)
        game.get_word(WORDS_DATABASE)
        game.update_word_hidden()
        show_start_banner(player_name)
        while game.lifes > 0:
            clear()
            show_game_title()
            print(f'\n{game}')
            if game.selected_word == game.selected_word_hidden:
                print('\n\tYou are RIGHT!!, Go to next round')
                input('\n\n\tPress ENTER to continue...')
                game.used_words.append(game.selected_word)
                while game.selected_word in game.used_words:
                    game.get_word(WORDS_DATABASE)
                game.used_letters.clear()
                game.update_word_hidden()
            else:
                user_input = input('\n\t>> CHOOSE LETTER: ').strip().lower()
                if user_input in game.abecedary:
                    if user_input in game.used_letters:
                        print('\nYou already chose this letter previously!!!')
                        time.sleep(2)
                    else:
                        game.used_letters.append(user_input)
                        game.update_word_hidden()
                        if user_input not in game.selected_word:
                            game.lifes -= 1
                            if game.lifes > 1:
                                game.n_factor += 5
                            else:
                                game.n_factor += 3
                else:
                    print('\n\tInvalid character!!!')
                    time.sleep(2)
        clear()
        show_game_title()
        print(f'\n\n\tG A M E   O V E R ! ! !\n'
            f'\n\tThe word was -> {game.selected_word.upper()}\n\n')
        updated_records = game.update_records(records)
        input('\tPress ENTER to continue...')
        while retry:
            clear()
            show_game_title()
            print()
            game.show_game_resume()
            print('\n\n     (1)RETRY    (2)CHANGE PLAYER    (0)MAIN MENU')
            user_input = input('\n\t\t>> SELECT: ').strip()
            if user_input == '1':
                ask_player_name = False
                break
            elif user_input == '2':
                ask_player_name = True
                break
            elif user_input == '0':
                retry = start_game = False
            else:
                print('\n\t\tInvalid option!!!')
                time.sleep(2)
        
    return updated_records