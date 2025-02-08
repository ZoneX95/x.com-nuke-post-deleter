import tweepy
from threading import Thread
import time

consumer_key = ""
consumer_secret = ""
access_key = ""
access_secret = ""

def delete_tweet(api, tweet_id):
    try:
        api.destroy_status(tweet_id)
        print(f"Deleted: {tweet_id}")
    except tweepy.errors.TweepyException as e:
        print(f"Failed to delete: {tweet_id}. Error: {e}")

def batch_delete(api):
    print(f"You are about to delete all tweets from the account @{api.verify_credentials().screen_name}.")
    print("Does this sound ok? There is no undo! Type 'yes' to carry out this action.")
    do_delete = input("> ").lower()
    if do_delete == 'yes':
        threads = []
        for status in tweepy.Cursor(api.user_timeline).items():
            if len(threads) >= 50:
                for t in threads:
                    t.join()
                threads = []
            thread = Thread(target=delete_tweet, args=(api, status.id))
            thread.start()
            threads.append(thread)
            time.sleep(0.1)
        
        for thread in threads:
            thread.join()
    else:
        print("Deletion canceled.")

if __name__ == "__main__":
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    
    try:
        print(f"Authenticated as: {api.verify_credentials().screen_name}")
        batch_delete(api)
    except tweepy.errors.TweepyException as e:
        print(f"Authentication or API error: {e}")