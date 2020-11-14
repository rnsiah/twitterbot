import tweepy

ACCESS_TOKEN = '54672015-RjfyiW99J1Yf9pxFy0YIHnHAHOVPjk4m4crCtPaCU'
ACCESS_TOKEN_SECRET = 'gukMmY5hEJEAx4BFXbIsejFeMRykjBT6ivx8PbLlT8P4z'
API_KEY = 'tcojsCGk6zh2FwrFNUi8GmEcG'
API_SECRET_KEY = 'RDrd3Mq5Co5zaxKce8ArPjjDZOad3KC31csgEM0telbxY8qaq3'

auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)

auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)
api.update_status(status='Morehouse Raised Me')
