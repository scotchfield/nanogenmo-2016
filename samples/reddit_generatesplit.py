import glob
import markovify
import random

subreddit = 'nosleep'
cache_dir = '../text/cache/' + subreddit + '/'

st_beginning = ''
st_middle = ''
st_end = ''


for filename in glob.glob(cache_dir + '*.txt'):
    input_file = open(filename, 'r')
    st = input_file.read()
    st_beginning += st.split('\n')[0]
    st_middle += '\n'.join(st.split('\n')[1:-1])
    st_end += st.split('\n')[-1]
    input_file.close()

model_beginning = markovify.Text(st_beginning)
model_middle = markovify.Text(st_middle)
model_end = markovify.Text(st_end)

out = []

words = 0


def make_sentence(section):
    if section == "beginning":
        return model_beginning.make_sentence()
    if section == "middle":
        return model_middle.make_sentence()
    if section == "end":
        model_end.make_sentence()


def make_story():
    story = []
    story.append("---------------\nTITLE\n----------\n\n")
    for i in range(random.randrange(4, 11)):
        story.append(make_sentence("beginning"))
    story.append("\n\n")
    for i in range(random.randrange(1, 7)):
        for i in range(random.randrange(11, 22)):
            story.append(model_middle.make_sentence())
        story.append("\n\n")
    for i in range(random.randrange(1, 4)):
        story.append(model_end.make_sentence())
    story2 = ' '.join(story)
    return story2

out.append(make_story())
out.append(make_story())

# out.append(model_beginning.make_short_sentence(35))
# out.append(model_middle.make_short_sentence(70))
# out.append(model_end.make_short_sentence(35))
print '\n\n\n\n'.join(out)

with open("output.txt", "w") as text_file:
    text_file.write('\n\n\n\n'.join(out))
