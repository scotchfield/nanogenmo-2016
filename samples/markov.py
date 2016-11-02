import random
from bisect import bisect

input_file = open('../text/firstnames.txt', 'r')
names = input_file.read().strip().split('\n')


def tupler(freq, letter):
    freqx = freq[letter]
    keys = freqx.keys()
    alles = []
    for key in keys:
        alles.append((key, freqx[key]))
    return alles


def weighted_choice(choices):
    values, weights = zip(*choices)
    total = 0
    cumulative_weights = []
    for w in weights:
        total += w
        cumulative_weights.append(total)
    x = random.random() * total
    i = bisect(cumulative_weights, x)
    return values[i]


def freq_finder(names):
    freq_obj = {}
    for name in names:
        last_c = ''
        name = name.lower()
        for c in name:
            if c not in freq_obj:
                freq_obj[c] = {}

            if last_c is not '':
                freq_obj[last_c][c] = freq_obj[last_c].get(c, 0) + 1

            last_c = c
    return freq_obj


def wordmaker(freq):
    word = random.choice(freq.keys())
    for i in range(random.randint(2, 7)):
        word += weighted_choice(tupler(freq, word[-1]))
    return word

print wordmaker(freq_finder(names)).title()
