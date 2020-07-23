import random

distribution = [
    ('a',9,1),
    ('b',2,3),
    ('c',2,3),
    ('d',4,2),
    ('e',12,1),
    ('f',2,4),
    ('g',3,2),
    ('h',2,4),
    ('i',9,1),
    ('j',1,8),
    ('k',1,5),
    ('l',4,1),
    ('m',2,3),
    ('n',6,1),
    ('o',8,1),
    ('p',2,3),
    ('q',1,10),
    ('r',6,1),
    ('s',4,1),
    ('t',6,1),
    ('u',4,1),
    ('v',2,4),
    ('w',2,4),
    ('x',1,8),
    ('y',2,4),
    ('z',1,10),
    ('*',2,0)
    ]

def calcPoints(combo):
    total = 0
    n = 0
    for letter1 in combo:
        for letter2 in distribution:
            if letter1 == letter2[0]:
                n += 1
                total += letter2[2]
    if n == len(combo):
        return total
    else:
        return 0

tileSet = []
for letter in distribution:
    for i in range(letter[1]):
        tileSet.append(letter)

set46 = []
for i in range(len(tileSet)):
    points = tileSet[i][2]
    for j in range(len(tileSet)):
        if i > j:
            points += tileSet[j][2]
            for k in range(len(tileSet)):
                if j > k:
                    points += tileSet[k][2]
                    for l in range(len(tileSet)):
                        if k > l and points >= 2:
                            points += tileSet[l][2]
                            for m in range(len(tileSet)):
                                if l > m and points >= 12:
                                    points += tileSet[m][2]
                                    for n in range(len(tileSet)):
                                        if m > n and points >= 22:
                                            points += tileSet[n][2]
                                            for o in range(len(tileSet)):
                                                if n > o and points >= 32:
                                                    points += tileSet[o][2]
                                                    if points == 42:
                                                        newCombo = tileSet[i][0] + tileSet[j][0] + tileSet[k][0] + tileSet[l][0] + tileSet[m][0] + tileSet[n][0] + tileSet[o][0]
                                                        if newCombo not in set46:
                                                            set46.append(newCombo)
                                                    points -= tileSet[o][2]
                                            points -= tileSet[n][2]
                                    points -= tileSet[m][2]
                            points -= tileSet[l][2]
                    points -= tileSet[k][2]
            points -= tileSet[j][2]
                                                        
for combo in set46:
    print(str(combo) + ' = ' + str(calcPoints(combo)))
                                                


def samePlace():
    tileSetShuffle = tileSet.copy()
    sameList = []
    for i in range(100000):
        random.shuffle(tileSetShuffle)
        same = 0
        for j in range(len(tileSet)):
            if tileSet[j] == tileSetShuffle[j]:
                same+=1
        sameList.append(same)

    average = sum(sameList) / len(sameList)
    print(average)

