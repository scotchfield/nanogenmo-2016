import glob
import markovify
import random

subreddit = 'nosleep'
cache_dir = '../text/cache/' + subreddit + '/'

st = ''

for filename in glob.glob( cache_dir + '*.txt' ):
    input_file = open( filename, 'r' )
    st += input_file.read() + '\n'
    input_file.close()

model = markovify.Text( st )

for i in range( random.randint( 3, 8 ) ):
    st = []

    for j in range( random.randint( 3, 8 ) ):
        st.append( model.make_sentence() )

    print ' '.join( st ) + '\n\n'
