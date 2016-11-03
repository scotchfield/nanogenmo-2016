import markovify
import random

input_file = open( '../text/nosleep.txt', 'r' )

st = input_file.read()

model = markovify.Text( st )

for i in range( random.randint( 3, 8 ) ):
    st = []

    for j in range( random.randint( 3, 8 ) ):
        st.append( model.make_sentence() )

    print ' '.join( st ) + '\n\n'
