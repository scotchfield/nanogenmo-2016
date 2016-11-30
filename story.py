import glob
import markovify
import random
import re

# fetch the cache (run reddit_cache.py in the samples dir to make one)

subreddit = 'nosleep'
cache_dir = './text/cache/' + subreddit + '/'

# initialise globals :/

st_beginning = ''
st_middle = ''
st_end = ''

out = ''

# make lists of adjectives and objects from txt files


def get_from_file(input_filename):
    input_file = open(input_filename, 'r')
    return input_file.read().strip().split("\n")

adjectives = get_from_file('./text/scary-adjectives.txt')
objects = get_from_file('./text/objects.txt')

# split the source material into beginnings, middles and ends

for filename in glob.glob(cache_dir + '*.txt'):
    input_file = open(filename, 'r')
    st = input_file.read()
    st_beginning += st.split('\n')[0]
    st_middle += '\n'.join(st.split('\n')[1:-1])
    st_end += st.split('\n')[-1]
    input_file.close()

# create markov using the split lists

model_beginning = markovify.Text(st_beginning)
model_middle = markovify.Text(st_middle)
model_end = markovify.Text(st_end)

# function to create a sentence based on what kind of sentence you want


def make_sentence(section):
    if section == "beginning":
        return model_beginning.make_sentence()
    if section == "middle":
        return model_middle.make_sentence()
    if section == "end":
        model_end.make_sentence()

# function to create a story of variable length and with a generated title


def make_story():
    story = []
    title = "The " + random.choice(adjectives) + " " + random.choice(objects)
    story.append("---------------\n" + title + "\n---------------\n\n")
    for i in range(random.randrange(4, 11)):
        story.append(make_sentence("beginning"))
    story.append("\n\n")
    for i in range(random.randrange(1, 10)):
        for i in range(random.randrange(7, 25)):
            story.append(model_middle.make_sentence())
        story.append("\n\n")
    for i in range(random.randrange(1, 4)):
        story.append(model_end.make_sentence())
    story2 = ' '.join(story)
    return story2


# find the word count

def wordCount(st):
    return len(re.findall(r'\b\w+\b', st))

# keep making stories until we get over book length

while wordCount(out) < 55000:
    out += make_story() + "\n\n\n\n"
    print str(wordCount(out)) + " words generated"

print out

# create a text file with your book

with open("output.txt", "w") as text_file:
    text_file.write(out)
