# Vraag namen op van deelnemers
# Controleer telkens of een ingevoerde naam wel uniek is
# Als er meer dan 2 namen zijn opgegeven kunnen er lootjes worden getrokken
# Maak lootjes voor alle namen
# Trek voor alle namen willekeurig (random) een lootje
# Iedereen heeft dus één uniek lootje
# Niemand mag het lootje van zichzelf hebben getrokken
# Print een lijst met namen en bijbehorende lootjes
import random

namen = []
namencheck = []
lootjes = []

vraag = int(input("Hoeveel deelnemers zijn er?: ")) 
for x in range(vraag):
    vraag2 = input("Wat zijn de namen van de deelnemers?\n: ")
    namen.append(vraag2)
    lootjes.append(vraag2)
    print("Naam:",vraag2,", toegevoegd.")
namen = list(set(namen))
lootjes = list(set(lootjes))
print(namen)

n = len(namen)
m = 0
temp = []
while m != n:
    x = random.randint(0,n-1)
    y = random.randint(0,n-1)
    if x != y:
        v = 0
        if len(temp) != 0:
            for i in range(len(temp)):
                if str(y) == temp[i][1] or str(x) == temp[i][0]:
                    v += 1
        if v == 0:
            temp.append(str(x) + str(y))
            print(namen[x], "heeft", namen[y])
            m += 1
