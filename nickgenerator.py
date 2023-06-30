import random
def CreateUsername():
    nicknamewords = [['your', 'lovely', 'love', 'honey', 'pretty'], ['frenchie', 'Frenchie'],
                     ['Girl', 'XO', 'Baby', 'GF'], [num for num in range(1, 100) if num not in [14, 88, 69]]]
    nickname = ''
    for i in nicknamewords:
        random_index = random.randint(0, len(i) - 1)
        nickname += str(i[random_index])
    return nickname
