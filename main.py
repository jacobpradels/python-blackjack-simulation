import random
import players
import decisions
singleDeck = [2,3,4,5,6,7,8,9,10,10,10,10,11]*4
currentDeck = singleDeck.copy()
currentDeck = currentDeck*6
random.shuffle(currentDeck)

global runningcount
runningcount = 0
player1 = players.player(10000)
dealer = players.dealer()
playerList = [player1, dealer]

def drawCard():
    global runningcount
    card = currentDeck.pop(random.randint(0,len(currentDeck)-1))
    if card < 7:
        runningcount += 1
    elif card > 9:
        runningcount -= 1
    return card

def startHand():
    for g in range(2):
        for x in range(len(playerList)):
            playerList[x].hand.append(drawCard())

def checkAces(player):
    if (player.total > 21 and 11 in player.hand):
        for card in range(len(player.hand)-1,):
            if player.hand[card] == 11:
                player.hand[card] = 1
                player.total = sum(player.hand)
                break


def playHand(player):
    if isinstance(player, players.player):
        player.total = sum(player.hand)
        # print(player.total)
        checkAces(player)
        try:
            playerdec = [decisions.xrow.index(dealer.hand[0]),decisions.ycol.index(player.total)]
            print(decisions.decisions[playerdec[1]][playerdec[0]])
            playvalue = decisions.decisions[playerdec[1]][playerdec[0]]
            if playvalue == 0:
                player.hand.append(drawCard())
                player.total = sum(player.hand)
                if (player.total < 17):
                    playHand(player)
            elif playvalue == 2:
                player.hand.append(drawCard())
                # return -1
        except:
            if player.total < 17:
                player.hand.append(drawCard())
                playHand(player)
    else:
        checkAces(player)
        player.total = sum(player.hand)
        if (player.total < 17):
            player.hand.append(drawCard())


# startHand()
def runGame():
    for x in playerList:
        x.hand.clear()
        for g in range(2):
            x.hand.append(drawCard())
        if playHand(x) == -1:
            continue
    for player in playerList:
        if isinstance(player, players.player):
            if player.total < 22 and dealer.total < 22 and player.total > dealer.total:
                print('player wins')
            elif player.total > 22:
                print('player loses')
            elif player.total < 22 and dealer.total < 22 and player.total < dealer.total:
                print('player loses')
            elif player.total == dealer.total:
                print('push')
for i in range(10):
    runGame()

print(player1.hand)
print(dealer.hand)
print(runningcount)

