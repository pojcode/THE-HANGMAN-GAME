''' 
File with the Game class to use in The Hangman Game
'''
import json
import random, string

class Game:
    ''' Class to model all the main components of the game '''
    def __init__(self, player_name:str, life_graphics:dict):
        self.player_name = player_name
        self.life_graphics = life_graphics
        self.lifes = 7
        self.used_letters = list()
        self.used_words = list()
        self.abecedary = list(string.ascii_lowercase)
        self.hearts_up = '(\/) '
        self.hearts_down = ' \/  '
        self.n_factor = 0
        self.selected_word = ''
        self.selected_word_hidden = ''
        
    def get_word(self, words:tuple):
        self.selected_word = random.choice(words)
    
    def update_records(self, records:list):
        players_list = records[::2]
        scores_list = records[1::2]
        score = len(self.used_words)
        scores_list.append(score)
        scores_list = sorted(scores_list, reverse=True)
        index_score = scores_list.index(score)
        players_list.insert(index_score, self.player_name)
        if len(players_list) > 10:
            del players_list[10:]
            del scores_list[10:]
        updated_records = []
        for i in range(len(players_list)):
            updated_records.append(players_list[i])
            updated_records.append(scores_list[i])
        self.records = updated_records

        return updated_records
    
    def update_word_hidden(self):
        word_hidden = ''
        for letter in self.selected_word:
            if letter in self.used_letters:
                word_hidden += letter
            else:
                word_hidden += '#'
        self.selected_word_hidden = word_hidden

    def show_game_resume(self):
        print(f'###| GAME RESUME |{"#"*37}\n')
        print(f'\t- Player Name: {self.player_name.upper()}\n'
            f'\t- Rounds: {len(self.used_words)}\n'
            f'\t- Words Guessed:')
        for word in self.used_words:
            print(f'\t\t· {word.upper()}')
        print('\n' + '#'*55)

    def __str__(self):
        game_view = f"LIFES {'-'*(28 - self.n_factor)}"
        game_view += f'{" "*(4 + self.n_factor)}USED LETTERS\n'
        game_view += f'{self.hearts_up * self.lifes}\n'
        game_view += f'{self.hearts_down * self.lifes}'
        game_view += f'{" "*(4 + self.n_factor)}' \
                    f'{" ".join(sorted(self.used_letters)).upper()}\n'
        game_view += f'\t\t{self.life_graphics[str(self.lifes)]}\n\n'
        game_view += f'\t-- HIDDEN WORD ->  ' \
                    f'{"-".join(self.selected_word_hidden.upper())}'

        return game_view
    
    def __del__(self):
        filename = 'the_hangman_data/the_hangman_records.json'
        with open(filename, 'w') as file_obj:
            json.dump(self.records, file_obj)