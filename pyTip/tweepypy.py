import tweepy
import csv
import pandas as pd
from .models import PyTip

# Twitter API credentials
consumer_key = "xxxxxx"
consumer_secret = "xxxxxxx"
access_key = "xxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxx"
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

#


def collect_all_tweets():
    username = 'python_tip'
    screenname = 'python_tip'
    max_tweets = 1000
    # tweets = api.user_timeline(screenname, count=10)

    tweets = tweepy.Cursor(api.user_timeline, id=username,
                           tweet_mode='extended').items(max_tweets)

    # for i in tweets:
    #     print(i.full_text)
    return tweets

    # collect_all_tweets()


def save_to_db():
    collected_tweets = collect_all_tweets()
    print(collected_tweets)
    for twit in collected_tweets:
        # print('worked here', twit.id)
        if not PyTip.objects.filter(tweet_id=twit.id):
            # print(twit.id_str, twit.full_text)
            add_tweet = PyTip(tweet_id=twit.id_str, tweet_text=twit.full_text,
                              timestamp=twit.created_at, tweet_link=f"https://twitter.com/{twit.user.screen_name}/status/{twit.id_str}", like=twit.favorite_count, retweet=twit.retweet_count, posted_by=twit.user.screen_name)
            add_tweet.save()