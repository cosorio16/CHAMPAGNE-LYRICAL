import tweepy

# oauth2_user_handler = tweepy.OAuth2UserHandler(
#     client_id=Client_ID,
#     redirect_uri="https://twitter.com/crtfdlvrby",
#     scope=["tweet.read", "tweet.write", "users.read"],
#     client_secret=Client_Secret
# )


# print(oauth2_user_handler.get_authorization_url())
# URL = input('Link here: ')
# TOKEN = oauth2_user_handler.fetch_token(URL)
# print(TOKEN)

TOKEN = ''
client = tweepy.Client(bearer_token=TOKEN)

client.create_tweet(
    user_auth=False,
)