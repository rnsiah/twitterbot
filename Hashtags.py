import tweepy
import pandas as pd
import os
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


max_tweets = 500

def get_twitter_api():
    ACCESS_TOKEN = '54672015-RjfyiW99J1Yf9pxFy0YIHnHAHOVPjk4m4crCtPaCU'
    ACCESS_TOKEN_SECRET = 'gukMmY5hEJEAx4BFXbIsejFeMRykjBT6ivx8PbLlT8P4z'
    API_KEY = 'tcojsCGk6zh2FwrFNUi8GmEcG'
    API_SECRET_KEY = 'RDrd3Mq5Co5zaxKce8ArPjjDZOad3KC31csgEM0telbxY8qaq3'

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth, wait_on_rate_limit=True)
    return api


df = pd.DataFrame(columns=  ['text', 'source', 'url'])

    tweet =[]
    tweets = []

    for tweets in tweepy.Cursor(api.search, q='lovewins', rpp=100).items(max_tweets):
        tweet = [tweet.text, tweet.source, tweet.source_url]
        tweet = tuple(tweet)
        tweets.append(tweet)

        df = pd.DataFrame(tweets)


def main2():
    get_tweets_from_hastag(df)



