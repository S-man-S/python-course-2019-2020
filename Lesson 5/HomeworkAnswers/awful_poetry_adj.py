import random
import sys

STROPHE_SIZE = 6   # количество строк стихотворения в одной строфе

particles = ["a", "the", "her", "his", "another", "the other", "my", "our", "mine", "their", "your", "one", "no"]
nouns = ["cat", "dog", "man", "woman", "boy", "girl", "granny", "wife", "boss", "horse", "mate", "daddy", 
         "friend","squirrel"]
verbs = ["sang", "ran", "jumped", "heard", "answered", "went", "told", "hoped", "felt", "slept", "hopped", "cried",
        "laughed", "walked", "dug", "came"]
adverbs = ["loudly", "quietly", "well", "badly", "slowly", "politely", "rudely", "indeed", "instead", "rarely", 
           "recently", "already", "blindly", "brightly", "clearly", "deeply", "easily", "exactly", "friendly",
           "happily", "hardly", "kindly", "lately", "madly", "perfectly", "politely", "rarely", "slowly", "warmly"]

adjectives = []

# по умолчанию количество строк стихотворенния равно размеру строфы
max_lines = STROPHE_SIZE

# обработка параметров командной строки
if len(sys.argv) > 1:
    try:
        temp = int(sys.argv[1])
        if 1 <= temp <= 100:
            max_lines = temp
        else:
            print("max_lines must be 1-100 inclusive")
    except ValueError:
        print("usage: awful_poetry_adj.py [lines] [noun_file] [verb_file] [adjective_file]")

    if len(sys.argv) > 2:
        noun_file = open(sys.argv[2], "r")
        for line in noun_file:
            nouns.append(line.strip())
        noun_file.close()

    if len(sys.argv) > 3:
        verb_file = open(sys.argv[3], "r")
        for line in verb_file:
            verbs.append(line.strip())
        verb_file.close()

    if len(sys.argv) > 4:
        adj_file = open(sys.argv[4], "r")
        for line in adj_file:
            adjectives.append(line.strip())
        adj_file.close()

# список использованных частей речи
used_parts = []

random.seed()
for index in range(max_lines):
    # получение частей речи с исключением дубликатов в рамках одной строфы
    particle = random.choice(particles);
    while particle in used_parts:
        particle = random.choice(particles);

    noun = random.choice(nouns);
    while noun in used_parts:
        noun = random.choice(nouns);

    verb = random.choice(verbs);
    while verb in used_parts:
        verb = random.choice(verbs);

    # пополнение списка использованных частей речи
    used_parts += [particle] + [noun] + [verb]

    # генерация строки стихотворения
    if random.randint(0,1) == 0:
        if adjectives and random.randint(0,2) in (0,1):  # 2/3 случаев когда нет наречий
            adjective = random.choice(adjectives)
            while adjective in used_parts:
                adjective = random.choice(adjectives)
            used_parts.append(adjective)
            print(particle, adjective, noun, verb)
        else:
            print(particle, noun, verb)
    else:
        adverb = random.choice(adverbs)
        while adverb in used_parts:
            adverb = random.choice(adverbs)
        used_parts.append(adverb)
        print(particle, noun, verb, adverb)

    # обработка конца строфы
    if (index + 1) % STROPHE_SIZE == 0:
        used_parts.clear()
        print()

input("Press enter to exit")
