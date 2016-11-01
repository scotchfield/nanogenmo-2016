import random

input_file = open( '../text/scary-adjectives.txt', 'r' )
scary_adjectives = input_file.read().strip().split( '\n' )

print 'The night was ' + random.choice( scary_adjectives ) + '!!!'
