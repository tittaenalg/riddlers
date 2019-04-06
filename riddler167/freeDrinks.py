from sys import argv
from random import randint

cards = [50, 50]
drinksStillOnOtherCard = 0
drinksRemainingTally = 0
simsRun = 0
simsToRun = int(argv[1])

def pickCardToUse():
    return randint(0,1)

def getDrink(card):
    cards[card] -= 1

outputFile = open("output.txt", "w")

while simsRun < simsToRun:
    while cards[0] >= 0 and cards[1] >= 0:
        getDrink(pickCardToUse())
    
    if cards[0] > 0 or cards[1] > 0:
        drinksStillOnOtherCard += 1

    drinksRemainigThisRound = cards[0] if cards[0] > 0 else 0 + cards[1] if cards[1] > 0 else 0
    drinksRemainingTally += drinksRemainigThisRound
    outputFile.write(str(drinksRemainigThisRound) + "\n")
    
    cards = [50, 50]
    simsRun += 1

outputFile.close()

print("Odds there is a drink on the other card: {}%".format(drinksStillOnOtherCard / simsToRun * 100))
print("Average drinks on other card: {}".format(drinksRemainingTally / simsToRun))