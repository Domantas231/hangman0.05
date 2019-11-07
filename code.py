class ch():
    def __init__(self, char, guessed):
        self.char = char
        self.guessed = guessed

file = 'words.txt'

with open(file, 'r') as f:
    data = f.split('\n')

def random():
        word = random.choice(data)
        return word

def convert(word):
    word1 = []
    for s in word:
        word1.append(ch(s, 0))

def isin(a, word):
    for s in word:
        if(a == s.char):
            for j in word:
                if a == j.char:
                    j.guessed = 1

            return True

    return False

lives = 6
word = convert(random())
while lives > 0:
    for s in word:
        print s.char, if s.guessed = 1 else print _ ,    

    a = raw_input("your lives: " + str(lives) + ", please guess: ")
    if not isin(a, word):
        lives -= 1

