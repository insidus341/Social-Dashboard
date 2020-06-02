import tweepy


def get_twitter_follower_count():
    auth = tweepy.OAuthHandler('8xIc3c3PeUZr2iaqCNmL7ncBz', '2K1FZt25HOYbLeLDuBUHXDr27RhyN7qplh10umG8EoyMmuJ3Lt')
    auth.set_access_token('1266351719556005888-EqS3P3C1WzGcSk6rEA1AENocLYmmMG', '8KWRtlsSs5iwyBUJPPcAHqiUrNKCPSH0ZZqb00TKRPrdt')

    twitter_api = tweepy.API(auth)
    user = twitter_api.get_user('jamesvscode')

    id_str = '1266351719556005888'

    try:
        response = twitter_api.followers(id_str)
        my_followers = len(response)
        return my_followers

    except Exception as e:
        raise Exception


if __name__ == '__main__':
    exit()