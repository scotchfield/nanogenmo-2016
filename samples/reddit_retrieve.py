import praw

subreddit = 'nosleep'

p = praw.Reddit( user_agent='nanogenmo_' + subreddit )
submissions = p.get_subreddit( subreddit ).get_hot( limit=1000 )

output_file = open( '../text/' + subreddit + '.txt', 'w' )

for submission in submissions:
    output_file.write( submission.selftext.encode('utf-8').strip() )

output_file.close()
