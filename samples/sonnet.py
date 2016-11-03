import markovify


def syllables(word):
    count = 0
    vowels = 'aeiouy'
    word = word.lower().strip(".:;?!")
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index-1] not in vowels:
            count += 1
    if word.endswith('e'):
        count -= 1
    if word.endswith('le'):
        count += 1
    if count == 0:
        count += 1
    return count


with open("../text/sonnets.txt") as f:
    text = f.read()

text_model = markovify.Text(text)

i = 0
while i < 12:
    sentence = (text_model.make_short_sentence(200))
    sentence_split = sentence.split()
    syllablecount = 0
    for word in sentence_split:
        syllablecount += syllables(word)
    if syllables(sentence) == 10:
        print sentence
        i += 1
