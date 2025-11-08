# app/core/poster.py
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("TWITTER_API_KEY"),
    consumer_secret=os.getenv("TWITTER_API_SECRET"),
    access_token=os.getenv("TWITTER_ACCESS_TOKEN"),
    access_token_secret=os.getenv("TWITTER_ACCESS_SECRET")
)

auth = tweepy.OAuth1UserHandler(
    os.getenv("TWITTER_API_KEY"),
    os.getenv("TWITTER_API_SECRET"),
    os.getenv("TWITTER_ACCESS_TOKEN"),
    os.getenv("TWITTER_ACCESS_SECRET")
)
api_v1 = tweepy.API(auth)

def post_thread_with_image(texts: list, image_path: str):
    """Post full thread with image on first tweet."""
    try:
        media = api_v1.media_upload(image_path)
        first = client.create_tweet(text=texts[0], media_ids=[media.media_id])
        prev_id = first.data["id"]

        for text in texts[1:]:
            prev_id = client.create_tweet(text=text, in_reply_to_tweet_id=prev_id).data["id"]

        print(f"Thread posted! https://twitter.com/darkpooldata/status/{first.data['id']}")
    except Exception as e:
        print(f"Post failed: {e}")