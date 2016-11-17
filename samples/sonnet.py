import markovify
import markov


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


def vogonize():
    vogon_word = markov.wordmaker(markov.freq_finder('../text/nouns.txt')).title()
    return vogon_word


with open("../text/sonnets.txt") as f:
    text = f.read()

text_model = markovify.Text(text, state_size=1)

i = 0
while i < 12:
    sentence = (text_model.make_short_sentence(140))
    sentence_split = sentence.split()
    syllablecount = 0
    for word in sentence_split:
        word = vogonize()
        syllablecount += syllables(word)
    if syllables(sentence) == 10:
        print sentence
        i += 1
