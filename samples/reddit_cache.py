import os
import praw

subreddit = 'nosleep'
cache_dir = '../text/cache/' + subreddit + '/'

if not os.path.exists( cache_dir ):
    os.makedirs( cache_dir )

p = praw.Reddit( user_agent='nanogenmo_' + subreddit )
submissions = p.get_subreddit( subreddit ).get_hot( limit=100 )

for submission in submissions:
    filename = cache_dir + submission.id + '.txt'

    if not os.path.isfile( filename ):
        print 'Writing ' + filename
        output_file = open( filename, 'w' )
        output_file.write( submission.selftext.encode('utf-8').strip() )
        output_file.close()
    else:
        print 'Already cached ' + filename
