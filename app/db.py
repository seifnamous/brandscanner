import mysql.connector
from config import Config
import data
from model import ModeltextBlob



class Database:
    def __init__(self):
        self.name = "Twits"

    def create_db(self):
        for result in cursor.execute(sql_query, multi=True):
            pass
        connection.commit()
        cursor.close()
        connection.close()
        connection.disconnect()
        print("ok")

    def insert_info_tweets(self, hashtag, count, lang='en'):
        config = Config.config
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        list_tweets = data.TwitterMain().get_info_tweets(hashtag, count)
        for tweet_dict in list_tweets:
            clean_tweet = clean_tweet = ModeltextBlob().clean_tweet(tweet_dict['tweet_text'])
            tweet_dict['tweet_type'] = ModeltextBlob().predict_sentiment(clean_tweet)
            values_to_insert = (tweet_dict['tweet_id'], tweet_dict['tweet_hashtag'], tweet_dict['tweet_influencer_username'], tweet_dict['tweet_text'], tweet_dict['tweet_time'], tweet_dict['tweet_type'])
            query = "INSERT INTO tweets (tweet_id, tweet_hashtag, tweet_influencer_username, tweet_text, tweet_time, tweet_type) VALUES (%s, %s, %s, %s, %s, %s)"
            try:
                cursor.execute(query, values_to_insert)
            except mysql.connector.errors.IntegrityError:
                print("This tweet has been already added into database")
        connection.commit()
        cursor.close()
        connection.close()
        return list_tweets

    def insert_info_influencers(self, influencer_username, tweet_id):
        config = Config.config
        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()
        dict_influencer = data.TwitterMain().get_info_influencers(influencer_username)
        values_to_insert = (dict_influencer['influencer_id'], dict_influencer['influencer_username'], dict_influencer['influencer_followers'], tweet_id)
        query = "INSERT INTO influencers (influencer_id, influencer_username, influencer_followers, tweet_id) VALUES (%s, %s, %s, %s)"
        try:
            cursor.execute(query, values_to_insert)
        except mysql.connector.errors.IntegrityError:
            print("This (influencer, tweet) has been already added into database")
        connection.commit()
        cursor.close()
        connection.close()
