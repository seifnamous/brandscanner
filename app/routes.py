from flask import Blueprint, request, render_template
from data import TwitterMain
from config import Config
from db import Database
from visualize import Plot

tweet = Blueprint('tweet', __name__)

@tweet.route('/')
def index():
	return render_template('home.html')

@tweet.route('/home')
def home():
	return render_template('home.html')

@tweet.route('/enterData')
def enterData():
	return render_template('enterData.html')

@tweet.route('/displayTweets', methods=['POST', 'GET'])
def displayTweets():

	if request.method == 'POST':
		hashtag = request.form['hashtag']
		numberTweets = int(request.form['numberTweets'])
		list_tweets = Database().insert_info_tweets(hashtag, numberTweets)

		list_influencers = []

		for tweet_dict in list_tweets:
			influencer_username = tweet_dict['tweet_influencer_username']
			tweet_id = tweet_dict['tweet_id']
			influencer_dict = TwitterMain().get_info_influencers(influencer_username)
			influencer_dict['tweet_id'] = tweet_id
			list_influencers.append(influencer_dict)
			Database().insert_info_influencers(influencer_username, tweet_id)
		fig_np = Plot().plot_tweets(hashtag)
		fig = fig_np[0].get_figure()
		fig.savefig('static/plots/{}.png'.format(hashtag[1:]), transparent=True)
		return render_template('displayTweets.html', hashtag = hashtag, numberTweets = numberTweets, list_tweets=list_tweets, list_influencers = list_influencers, img='{}.png'.format(hashtag[1:]))
