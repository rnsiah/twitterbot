import tweepy
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt


max_tweets=200


def get_twitter_api():
    ACCESS_TOKEN = '54672015-RjfyiW99J1Yf9pxFy0YIHnHAHOVPjk4m4crCtPaCU'
    ACCESS_TOKEN_SECRET = 'gukMmY5hEJEAx4BFXbIsejFeMRykjBT6ivx8PbLlT8P4z'
    API_KEY = 'tcojsCGk6zh2FwrFNUi8GmEcG'
    API_SECRET_KEY = 'RDrd3Mq5Co5zaxKce8ArPjjDZOad3KC31csgEM0telbxY8qaq3'

    auth = tweepy.OAuthHandler(API_KEY, API_SECRET_KEY)

    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    api = tweepy.API(auth)
    return api


def collect_Twitter_Data_For_User(api, twitter_user):
    favorite_data = []
    retweet_data = []

    for status in tweepy.Cursor(api.user_timeline, id=twitter_user).items(100):
        favorite_data.append(status.favorite_count)
        retweet_data.append(status.retweet_count)

    return favorite_data, retweet_data


def main():
    api = get_twitter_api()
    favorite_data, retweet_data = collect_Twitter_Data_For_User(api, '@cnnbrk')
    print(favorite_data)
    print(retweet_data)
    print(len(favorite_data))
    print(len(retweet_data))

    #reshape data to columns

    retweet_data_col = np.array(retweet_data).reshape((-1, 1))
    print(retweet_data_col)

    regr = linear_model.LinearRegression()
    regr.fit(retweet_data_col, favorite_data)
    print('Coefficient:', regr.coef_)
    print('Intercepts:', regr.intercept_)

    x = np.array(range(0, max(retweet_data)))
    y = eval('regr.coef_* x + regr.intercept_')
    plt.scatter(retweet_data, favorite_data, color='red')
    plt.xlabel('Retweets')
    plt.ylabel('Favorited')
    plt.plot(x, y)
    plt.show()


if __name__ == '__main__':
    main()



