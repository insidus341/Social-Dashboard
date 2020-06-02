import requests


def get_youtube_subscriber_count():
    url = 'https://www.googleapis.com/youtube/v3/channels'
    channel_id = "UCpjOrUKSGSbXkfmkibKYbZA"
    api_key = 'AIzaSyBdajJfb2hfdCUqdsTwK8UxOXuXLkcNphE'

    request = requests.session()
    request.params = {
        "part": "statistics",
        "id": channel_id,
        "key": api_key
    }

    try:
        response = request.get(url).json()
        subscriber_count = response['items'][0]['statistics']['subscriberCount']

        return subscriber_count

    except Exception as e:
        raise Exception


if __name__ == '__main__':
    exit()