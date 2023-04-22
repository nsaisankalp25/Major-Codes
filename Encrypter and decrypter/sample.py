import random

def IndMixer() -> list:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    enLetters = []
    ran_num = random.randint(1,26)
    print(ran_num)
    for i in letters:
        ind = letters.index(i) + ran_num
        if ind > 26: ind -= 26
        enLetters.append(letters[ind-1])
    return [ran_num] + enLetters


print(IndMixer())