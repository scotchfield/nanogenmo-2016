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

out.append(model_beginning.make_sentence())

for i in range(random.randrange(2, 5)):
    out.append(model_middle.make_sentence())

out.append(model_end.make_sentence())

print ' '.join(out) + '\n\n'
