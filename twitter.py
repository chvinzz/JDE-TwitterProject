import tweepy

consumer_key = 'SNDhT4ZYKnM398eNo98HczpIC'    # my twitter API key & serect
consumer_serect = 'uEozE1tc7Fvlz5JbMWC4Ap8CkVvi3G9Vw9syu0rwsNfaNE8YkD'
access_token = '1447428831950688261-5LPYCfyhKdNW46Lc0JRIbIeTTw9KmA'
access_token_secret = 'mWyzY7sId3zRmKdXMUTduLyRgbG6SH2AXzV2SzxZ9hOmc'


auth = tweepy.OAuthHandler(consumer_key, consumer_serect)   #authentication
auth.set_access_token (access_token , access_token_secret)

api = tweepy.API(auth)
name = '@JoeBiden'
tweetCount =100   # return the 100 status(can change)
results = api.user_timeline(id=name, count=tweetCount)
for tweet in results:
    print(tweet)



