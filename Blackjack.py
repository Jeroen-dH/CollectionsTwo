import time
import re
import random
deck = ['A (11)',"Harten 2","Harten 3", "Harten 4", 'Harten 5', "Harten 6", "Harten 7", "Harten 8", "Harten 9 ", "Harten 10", "Harten Boer (10)", "Harten vrouw (10)", "Harten Koning (10)", 'A (11)',"klaver 2","klaver 3", "klaver 4", 'klaver 5', "klaver 6", "klaver 7", "klaver 8", "klaver 9 ", "klaver 10", "klaver Boer (10)", "klaver vrouw (10)", "klaver Koning (10)",'A (11)',"Schoppen 2","Schoppen 3", "Schoppen 4", 'Schoppen 5', "Schoppen 6", "Schoppen 7", "Schoppen 8", "Schoppen 9 ", "Schoppen 10", "Schoppen Boer (10)", "Schoppen vrouw (10)", "Schoppen Koning (10)",'A (11)',"ruiten 2","ruiten 3", "ruiten 4", 'ruiten 5', "ruiten 6", "ruiten 7", "ruiten 8", "ruiten 9 ", "ruiten 10", "ruiten Boer (10)", "ruiten vrouw (10)", "ruiten Koning (10)"]
dealer = []
player = []
dealercount = 0
playercount = 0
a = 0
dealerbust = 0

def addcarddealer(variable):
    for x in range(variable):
        dealer.append(random.choice(deck))
def addcardplayer(variable):
    for x in range(variable):
        player.append(random.choice(deck))

def hit():
    print("Je krijgt een kaart.")
    addcardplayer(1)
    playercount = 0
    for x in player:
        a = re.findall('\d+', x)
        x = ''.join(a)
        playercount = playercount + int(x)

def yes(dealercount, a):
    if dealercount < 17:
        a(1)
        dealercount = 0
        for x in dealer:
            a = re.findall('\d+', x)
            x = ''.join(a)
            dealercount = dealercount + int(x)
            if dealercount >21:
                global dealerbust
                dealerbust = True
                print("De dealer is bust")
    print("de dealer heeft: ",dealer)

print("Welkom bij blackjack!")
y = input("Druk op enter om te begginen")
time.sleep(0.5)
print("Kaarten worden uigedeeld.....")

addcardplayer(2)
print("\nJou kaarten zijn: ",player[0],"en", player[1])
for x in player:
    a = re.findall('\d+', x)
    x = ''.join(a)
    playercount = playercount + int(x)
print("samen is dit",playercount,"\n")

addcarddealer(2)
print("de dealer heeft:", dealer[0],", [X]")
for x in dealer:
    a = re.findall('\d+', x)
    x = ''.join(a)
    dealercount = dealercount + int(x)
if dealercount != 21:
    while playercount < 21:
        HitOrStand = input("Je kaarten hebben een waarde van: " + str(playercount) + ".\nWil je 'Hit' (nog een kaart pakken) of wil je 'Stand'(geen kaart pakken en de beurt doorgeven)")
        if HitOrStand == 'hit':
            print("Je krijgt een kaart.")
            addcardplayer(1)
            playercount = 0
            for x in player:
                a = re.findall('\d+', x)
                x = ''.join(a)
                playercount = playercount + int(x)
            print("je heb nu",player,", Waarde: ",playercount,)
        elif HitOrStand == 'stand':
            print("je stand.")
            print("De dealer heeft",dealer[0], dealer[1])
            yes(dealercount, addcarddealer)
            break
else: 
    print("dealer heeft blackjack")

if dealerbust:
    print("Je hebt gewonnen, de dealer is bust!")
elif playercount > 21:
    print("Je bent bust!")
elif playercount > dealercount:
    print("Gefeliciteerd je hebt gewonnen!")
elif playercount == dealercount:
    print("Jij en de dealer hebben hetzelfde! het is gelijk spel.")
else:
    print("Je hebt helaas verloren..")