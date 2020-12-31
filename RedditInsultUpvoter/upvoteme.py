# WARNING: This technically breaks Reddit's rules. 
#          Probably shouldn't use this. 

peopleToUpvote = ['Benjiboy50fonz']

import praw

from prawcore.exceptions import BadRequest

reddit = praw.Reddit(
    client_id="60i7GSgGbmws3Q",
    client_secret="8x_B9id73OVRKMMcrc1OsdUdukNGaA",
    username="_Insult_Bot ",
    password="otnuwztq",
    user_agent="Insult"   
)

for person in peopleToUpvote:
    lg = reddit.redditors.search(person)
    
    for redditor_ in lg: # Take me from the ListingGenerator
        posts = redditor_.submissions.top("all")
        lengthP = redditor_.submissions.top("all")
        
    length = 0
    for x in lengthP: # There is no 'len' for ListingGenerator
        length += 1 
    
    count = 1
    
    for post in posts:
        try:
            post.upvote() # Upvotes every post I've made.
            print(str(count) + '/' + str(length))            
        except(BadRequest):
            print('Couldn\'t do it. Too old?')
            
        count += 1