import os
import random
import praw
from dotenv import load_dotenv

load_dotenv()
reddit = praw.Reddit(
    client_id=os.getenv("ID"),
    client_secret=os.getenv("SECRET"),
    user_agent="python:TheThornBot:v1.0 (by /u/Ok-Preference7616)",
    username=os.getenv("USERNAME"),
    password=os.getenv("PASSWORD")
)

while True:
    try:
        for post in reddit.subreddit("theletterthorn").stream.submissions(skip_existing=True):
            number = random.choice([0,1])
            if number == 0:
                post.reply("þ")
            else:
                post.reply("Þ")
    except Exception as e:
        print(e)
        if "invalid_grant" in str(e):
            print("log out and log in again on reddit.com to rectify this issue.")
            break
        else:
            continue
