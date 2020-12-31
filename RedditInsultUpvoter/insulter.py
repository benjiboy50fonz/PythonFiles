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
            parentComment = mention.parent()
            try:
                parentComment.reply(generateInsult())
            except(RedditAPIException):
                print("Uh oh, gotta wait.")
                
    except(ResponseException):
        print("401 Error . . . Retrying . . .")