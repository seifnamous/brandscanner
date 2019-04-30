# from data import TwitterMain
# print(TwitterMain().get_info_username('AlexanderRhodes'))


# from db import Database
# Database().insert_info_influencer('AlexanderRhodes', 'fffff')

# from model import ModeltextBlob
# tweet = "hey i love this product amazing produc"
# clean_tweet = ModeltextBlob().clean_tweet(tweet)
# print(ModeltextBlob().predict_sentiment(clean_tweet))


from visualize import Plot
Plot().plot_tweets('#usa')
