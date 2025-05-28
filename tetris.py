#Sadie Barash
#Tetris Score Analysis

#Init
# List of Tetris scores (unsorted)
scores = [
    3600460, 1388900, 5435960, 4222920, 8063900, 1362703, 6529560, 2043580, 1390000, 1696224,
    1372600, 2535840, 2605320, 2275996, 11966100, 1472600, 1390780, 1768400, 1333731, 1317580,
    1777456, 4899280, 2790920, 1626880, 1476400, 29486164, 4570640, 1649100, 4890220, 6492500,
    1614120, 5157860, 1582980, 1357480, 2382340, 1532660, 2378832, 1316520, 2529080, 13793540,
    1386260, 1352620, 1442340, 1406260, 1705680, 12409180, 2281848, 3222400, 1349060, 2302480,
    1571120, 3067100, 3740500, 1606732, 2153480, 2011360, 1344740, 1371060, 1345420, 2373940,
    1702940, 2077552, 2108820, 1322485, 1404800, 2555620, 1405580, 4213540, 3835120, 6563440,
    1350742, 1537800, 1657560, 1333995, 1632505, 2743060, 1509751, 1554880, 1316540, 1323680,
    2433160, 1340460, 1659860, 1608500, 7220241, 1834120, 7081880, 1483360, 16700760, 1435280,
    1702640, 1371040, 1316900, 2114180, 1374100, 1412260, 1379220, 1319573, 1623160, 6787420
]


#Functions
def high_score(): #Find highest score
    highestScore=0
    for score in scores:
        if score>highestScore:
            highestScore=score
    return (highestScore)

def low_score():
    lowestScore=10000000000000
    for score in scores:
        if score<lowestScore:
            lowestScore=score
    return (lowestScore)

def avg_score():
    total=0
    for i in range(len(scores)):
        total=total+scores[i]
        average=total/100
    print(average)

def input_score():
    new=input("Please enter a score")
    new=int(new)
    if new>high_score():
        print("Congrats! You have the new high score!")
    if new<low_score():
        print("Score is not in the top 100 - rejected.")
    if new>low_score():
        scores.remove(low_score())
        scores.append(new)
        print("Your score is in the top 100! Congrats!")




#Main

print("Welcome to Tetris DataBase")
print("""What would you like to do:
      1. See high score
      2. See low score
      3. See average score in top 100
      4. Input a score""")
choice=input("What would you like to do (1-4)")
if choice==1:
    print(high_score())
if choice==2:
    print(low_score())
if choice==3:
    avg_score()
if choice==4:
    input_score()



