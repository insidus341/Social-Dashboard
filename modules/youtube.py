import requests
from modules.get_environmentals import youtube_api_key, youtube_channel_id


def get_youtube_subscriber_count():
    url = 'https://www.googleapis.com/youtube/v3/channels'

    request = requests.session()
    request.params = {
        "part": "statistics",
        "id": youtube_channel_id,
        "key": youtube_api_key
    }

    try:
        print("Getting YouTube Subscribers")
        response = request.get(url).json()
        subscriber_count = response['items'][0]['statistics']['subscriberCount']

        return subscriber_count

    except Exception as e:
        print('YouTube API failed')
        raise Exception


if __name__ == '__main__':
    exit()