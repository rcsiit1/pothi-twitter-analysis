from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json

APP_KEY = ''
APP_SECRET = ''
access_token= ''
access_token_secret =''

#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        tweets = json.loads(data)
        if 'full_text' in tweets and tweets['truncated'] == 'True':
            print(tweets['full_text'],'\n')
        else:
            print(tweets['text'],'\n')
        return True

    def on_error(self, status):
        print(status)


def SearchTermsInTweets():
    search_key = input('Enter the search term \n')

    #This handles Twitter authetification and the connection to Twitter Streaming API
    listener = StdOutListener()
    auth = OAuthHandler(APP_KEY, APP_SECRET)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, listener)

    #This line filter Twitter Streams to capture data by the keywords taken as an input
    stream.filter(track= [search_key])



if __name__ == '__main__':

    SearchTermsInTweets()
