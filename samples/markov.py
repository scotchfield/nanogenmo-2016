import random

input_file = open( '../text/firstnames.txt', 'r' )
names = input_file.read().strip().split( '\n' )

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

word = random.choice( freq_obj.keys() )

for i in range( random.randint( 4, 7) ):
  word += random.choice( freq_obj[word[-1]].keys() )

print word
