import tweepy
from modules.get_environmentals import twitter_api_key, twitter_api_token, twitter_api_key_secret, \
    twitter_api_token_secret, twitter_username


def get_twitter_follower_count():
    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
    auth.set_access_token(twitter_api_token, twitter_api_token_secret)

    twitter_api = tweepy.API(auth)

    try:
        print('Getting Twitter Followers')
        response = twitter_api.get_user(twitter_username)
        my_followers = response.followers_count
        return my_followers

    except Exception as e:
        print("Twitter Failure")
        print(e)
        raise Exception


if __name__ == '__main__':
    exit()