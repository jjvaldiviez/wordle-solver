from database.word_db import get_word_options

grn = ['_','R','E','A','D']
yel = ['_','_','_','_','_']
gry = ['I','S','L','B','K']

options = get_word_options(grn, yel, gry)
guesses = [v for v in options if len(v) == 5]

print(guesses)