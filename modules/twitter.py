import tweepy
from modules.get_environmentals import twitter_api_key, twitter_api_token, twitter_api_key_secret, \
    twitter_api_token_secret, twitter_username


def get_twitter_follower_count():
    auth = tweepy.OAuthHandler(twitter_api_key, twitter_api_key_secret)
    auth.set_access_token(twitter_api_token, twitter_api_token_secret)

    twitter_api = tweepy.API(auth)
    user = twitter_api.get_user(twitter_username)

    id_str = user.id_str

    try:
        response = twitter_api.followers(id_str)
        my_followers = len(response)
        return my_followers

    except Exception as e:
        raise Exception


if __name__ == '__main__':
    exit()