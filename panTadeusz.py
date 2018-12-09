import math
#chars = '0123456789aąbcćdeęfghijklłmnńoópqrstuvwxyzAĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'
chars = '0123456789AĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

MORSE_CODE_DICT = { 'A':'.-', 'Ą':'.-.-', 'B':'-...', 
                    'C':'-.-.', 'Ć':'-.-..', 'D':'-..', 'E':'.', 
                    'Ę':'..-..','F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'Ł':'.-..-', 'M':'--', 'N':'-.', 'Ń':'--.--',
                    'O':'---', 'Ó':'---.', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'Ś':'...-...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 'Ż':'--.-.', 'Ź':'--..-', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ',':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ';':'-.-.-.', ':':'---...',
                    '"':'.-..-.', '!':'-.-.--'} 

def encrypt(message): 
    cipher = '' 
    for letter in message:
        if letter == '\n': continue 
        if letter != ' ':
            cipher += MORSE_CODE_DICT[letter]
        else: 
           cipher += 'x'
    return cipher 

def shanonEntrophy(data):
    if not data:
        return 0
    entropy = 0
    for i, x in enumerate(chars):
        p_x = float(data.count(x))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy

def getTextFromFile(inputFile):
    with open(inputFile, "r") as f:
        return f.read().upper()

def letterChance(text, char):
  count = 0
  for c in text:
    if char == c:
      count += 1 
  return (count * 100 )/ len(text)

text = getTextFromFile('panTadeusz.txt')

#chars = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
for i, char in enumerate(chars):
    print(char + " - " + str(letterChance(text, char)))

print('Entropia Shanona - ' , shanonEntrophy(text))

morse = encrypt(text)
#print(morse)

# file = open('morsTadeusz.txt', 'w') 
# file.write(morse) 
# file.close() 

print(". " + str(letterChance(morse, '.')))
print("- " + str(letterChance(morse, '-')))
print("Koniec znaku " + str(letterChance(morse, 'x')))

print('Entropia Shanona - morse ' , shanonEntrophy(morse))
