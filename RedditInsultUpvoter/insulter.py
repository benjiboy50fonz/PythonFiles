import requests
import praw

from prawcore.exceptions import ResponseException
from praw.exceptions import RedditAPIException

def generateInsult():
    response = requests.get("https://evilinsult.com/generate_insult.php?lang=en&type=json")
    return response.json()["insult"]

reddit = praw.Reddit(
    client_id="60i7GSgGbmws3Q",
    client_secret="8x_B9id73OVRKMMcrc1OsdUdukNGaA",
    username="_Insult_Bot ",
    password="otnuwztq",
    user_agent="Insult"   
)

while True:

    try:
        for mention in reddit.inbox.mentions():
            if mention.new: # Take the new, unread, mentions. 
                parentComment = mention.parent()
                try:
                    swearing = False
                    insult = generateInsult()
                    
                    if "fuck" in insult or "shit" in insult: # Keep it wholesome lol. 
                        swearing = True
                        while swearing:
                            insult = generateInsult()
                            if "fuck" not in insult and "shit" not in insult:
                                swearing = False
                                
                    parentComment.reply(insult) # Reply to whoever the bot was called upon. 
                    mention.mark_read()
                    print("Insulted!")
                except(RedditAPIException):
                    print("Uh oh, gotta wait.") # Posting too fast?
                
    except(ResponseException):
        print("Error . . . Retrying . . .") # No connection