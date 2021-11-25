#speciale tekens niet op eerste of laaste positie ook niet op vaste plek. 4 tot 7 cijfers. eerste 3 posities geen cijfers.
import string
import random
import time

alphabetLowercase = list(string. ascii_lowercase)
alphabetUppercase = list(string. ascii_uppercase)
numbers = list(string.digits)
symbols = ["@","#","$","%","&","_","?"]
password = []

for a in range(3):
    letters = [random.choice(alphabetLowercase),random.choice(alphabetUppercase)]
    randoms = random.choice(letters)
    password.append(randoms)
for a in range(18):
    alles = [random.choice(alphabetLowercase), random.choice(alphabetUppercase), random.choice(numbers),random.choice(symbols)]
    randoms = random.choice(alles)
    password.append(randoms)
for a in range(3):
    letters = [random.choice(alphabetLowercase),random.choice(alphabetUppercase)]
    randoms = random.choice(letters)
    password.append(randoms)

print("Gernerating password......")
time.sleep(1)
print(password)