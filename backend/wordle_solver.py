from backend.database.word_db import get_word_options

def get_guesses(grn, yel, gry):
    print("Converting guesses")
    grn = convert_grn(grn)
    yel = convert_yel(yel)
    print(f"Greens: {grn}\nYellows: {yel}\nGrays: {gry}\n")
    print("Retrieving Guesses\n")
    options = get_word_options(grn, yel, gry)
    return [v for v in options if len(v) == 5]

def convert_yel(yel):
    ret = [[],[],[],[],[]]
    for i in range(len(yel)):
        if yel[i] != '_':
            ret[i % 5].append(yel[i])
    return ret

def convert_grn(grn):
    ret = ['_','_','_','_','_']
    for i in range(len(grn)):
        if grn[i] != '_':
            ret[i % 5] = grn[i]
    return ret