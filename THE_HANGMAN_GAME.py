'''
The classical hangman game created in python
'''
import os
from the_hangman_files.the_hangman_main import main

def the_hang_man():
    os.system('mode con: cols=68 lines=27')
    main()
    
if __name__ == '__main__':
    the_hang_man()