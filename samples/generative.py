import random

def getFromFile( input_filename ):
    input_file = open(input_filename, 'r')
    return input_file.read().strip().split( '\n' )

scary_adjectives = getFromFile('../text/scary-adjectives.txt')
firstnames = getFromFile('../text/firstnames.txt')
moods = getFromFile('../text/moods.txt')
objects = getFromFile('../text/objects.txt')
occupations = getFromFile('../text/occupations.txt')

sentences = getFromFile('../text/scary-sentences.txt')

def getSentence():
    data = random.choice(sentences)

    replace_obj = [
        ('{object}', objects),
        ('{firstname}', firstnames),
    ]

    for replace in replace_obj:
        while data.find(replace[0]) > -1:
            data = data.replace(replace[0], random.choice(replace[1]))

    return data

def getParagraph():
    data = []

    for i in range(random.randint(3, 9)):
        data.append(getSentence())

    return ' '.join(data)

def getStory():
    data = []

    for i in range(random.randint(3, 9)):
        data.append(getParagraph())

    return '\n\n'.join(data)

print getStory()
