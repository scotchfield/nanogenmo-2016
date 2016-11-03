import praw

p = praw.Reddit( user_agent='nanogenmo_nosleep' )
submissions = p.get_subreddit( 'nosleep' ).get_hot( limit=10 )

output_file = open( '../text/nosleep.txt', 'w' )

for submission in submissions:
    output_file.write( submission.selftext.encode('utf-8').strip() )

output_file.close()
