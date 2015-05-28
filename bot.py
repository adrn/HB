#!/usr/bin/env python
import os
import random
import time
import tweepy
from keys import keys

CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

response_extras = ["",
                   "this is SICK",
                   "this is the BOMB"]
response = "dude. {0}"

cachefilename = "already-replied.txt"
if not os.path.exists(cachefilename):
    open(cachefilename, 'a').close()

if __name__ == "__main__":
    since = 0

    while True:
        with open(cachefilename) as f:
            already_replied = f.readlines()

        tweets = api.search(q="hoggbot", since_id=since)
        for s in tweets:
            if str(s.id) in already_replied:
                continue

            sn = s.user.screen_name
            msg = response.format(random.choice(response_extras))
            m = "@{username} {message}".format(username=sn, message=msg)

            print("Replying to {0}: {1}".format(sn, m))
            s = api.update_status(status=m, in_reply_to_status_id=s.id)

            with open(cachefilename, 'a') as f:
                f.write("{0}\n".format(str(s.id)))

        time.sleep(60)
