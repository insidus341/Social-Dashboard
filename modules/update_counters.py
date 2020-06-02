import json
import time

from modules.twitter import get_twitter_follower_count
from modules.youtube import get_youtube_subscriber_count


TIMER_OFFSET = 60


def get_counter():

    old_counters = get_stored_data()

    original_ts = old_counters['last_updated']
    now_ts = int(time.time())
    time_difference = now_ts - original_ts

    if time_difference > TIMER_OFFSET:
        try:
            new_counters = update_counter()
            update_storage(old_counters, new_counters)

            return get_stored_data()

        except Exception as e:
            response = {
                'error': '429'
            }

            return response

    else:
        return get_stored_data()


def update_counter():

    twitter_followers = None
    youtube_followers = None

    try:
        twitter_followers = get_twitter_follower_count()
        youtube_followers = get_youtube_subscriber_count()
    except Exception as e:
        raise Exception

    response = {
        "twitter_followers": twitter_followers,
        "twitter_percent": '.7',
        "youtube_subs": youtube_followers,
        "youtube_percent": ".8",
        "last_updated": int(time.time())
    }

    return response


def get_stored_data():

    with open("storage/counter_data.json", "r") as file:
        stored_counter_data_json = json.load(file)

    return stored_counter_data_json


def set_stored_data(counters):

    with open("storage/counter_data.json", "w") as file:
        json.dump(counters, file)


def calculate_percentage(current, target):

    percent = float(current) / float(target)
    return percent


def update_storage(counters, new_counters):

    counters['twitter_followers'] = new_counters['twitter_followers']
    counters['youtube_subs'] = new_counters['youtube_subs']
    counters['last_updated'] = new_counters['last_updated']

    counters['youtube_percent'] = calculate_percentage(
        counters['youtube_subs'],
        counters['youtube_subs_target']
    )

    counters['twitter_percent'] = calculate_percentage(
        counters['twitter_followers'],
        counters['twitter_followers_target']
    )

    set_stored_data(counters)


