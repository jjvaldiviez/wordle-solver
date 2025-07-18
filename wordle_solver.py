from database.word_db import get_word_options

grn = ['_','I','_','_','_']
yel = ['_','_','G','_','T']
gry = ['A','S','L','E','D','Y']

options = get_word_options(grn, yel, gry)
guesses = [v for v in options if len(v) == 5]

print(guesses)