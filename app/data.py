import pandas as pd
import tweepy
from utils import twit_auth_handler

class TwitterMain:
    def __init__(self):
         self.api = twit_auth_handler()

    def get_info_tweets(self, hashtag, count, lang='en'):
         list_tweets = []
         tweets = tweepy.Cursor(self.api.search, q=hashtag, lang=lang).items(count)
         for tweet in tweets:
             dic_tweet = {'tweet_id':tweet.id_str, 'tweet_hashtag':hashtag, 'tweet_influencer_username':tweet.user.screen_name, 'tweet_text':tweet.text, 'tweet_time':tweet.created_at.strftime('%Y-%m-%d %H:%M:%S'), 'tweet_type':'not known'}
             list_tweets.append(dic_tweet)
         return list_tweets

    def get_info_influencers(self, influencer_username):
        user = self.api.get_user(influencer_username)
        dict_influencer = {'influencer_id':user.id_str, 'influencer_username': user.screen_name, 'influencer_followers':user.followers_count}
        return dict_influencer
