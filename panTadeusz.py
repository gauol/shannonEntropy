import math
chars = '0123456789aąbcćdeęfghijklłmnńoópqrstuvwxyzAĄBCĆDEĘFGHIJKLŁMNŃOÓPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~'

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
        return f.read()

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

print('Entropia Shanona' + shanonEntrophy(text))
