DROP DATABASE IF EXISTS Twits;
CREATE DATABASE Twits;
use Twits;

CREATE TABLE tweets
(
tweet_id VARCHAR(50) PRIMARY KEY NOT NULL,
tweet_hashtag VARCHAR(50),
tweet_influencer_username VARCHAR(50),
tweet_text LONGBLOB,
tweet_time DATETIME,
tweet_type VARCHAR(10) DEFAULT 'not known'
);

CREATE TABLE influencers
(
influencer_id VARCHAR(50),
influencer_username VARCHAR(50),
influencer_followers INT,
tweet_id VARCHAR(50),
FOREIGN KEY(tweet_id) REFERENCES tweets(tweet_id),
PRIMARY KEY (influencer_id,tweet_id)
);
