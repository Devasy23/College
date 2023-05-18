import pandas as pd

dict = {'U1':{'M1':3,'M3':4, 'M6':1},
        'U2':{'M3':2, 'M4':2},
        'U3':{'M1':2, 'M2':4, 'M4':4, 'M5':4, 'M6':3},
        'U4':{'M1':1, 'M2':5, 'M3':2, 'M5':3},
        'U5':{'M3':1, 'M4':5, 'M5':4, 'M6':3},
        'U6':{'M1':4, 'M5':2},
        'U7':{'M2':4, 'M3':3}
        }

df = pd.DataFrame(dict)

# similarity using pearson correlation
import numpy as np
# import pandas as pd
 
def user_similarity(df):
    # calculate the similarity between two users via pearson correlation
    # user-user similarity matrix
    # df = df.T
    # substraction of mean from each user ratings
    df = df - df.mean(axis=1).values.reshape(-1,1)
    df = df.fillna(0)
    similarity = df.corr()
    return similarity


def item_similarity(df):
    # calculate the similarity between two items via pearson correlation
    # item-item similarity matrix
    df= df.T
    df = df - df.mean(axis=0).values.reshape(1,-1)
    df = df.fillna(0)
    similarity = df.corr()
    return similarity
ussim = user_similarity(df)
itsim = item_similarity(df)
def predict_rating(df, similarity, user, item):
    # predict the ratings for 'item' for 'user' consider the top 3 similar users
    df = df.T
    # similarity = similarity.T
    # get the top 3 similar users
    top3 = similarity[user].sort_values(ascending=False)[1:4]
    print(top3)
    # get the ratings of the top 3 similar users for item
    # df
    top3rating = df.loc[top3.index, item]
    # print(top3rating)
    # calculate the predicted rating
    rating = np.dot(top3, top3rating) / sum(top3)
    return rating


def predict_rating2(df, similarity, user, item):
    #  predict based on item-item similarity
    # predict the ratings for 'item' for 'user' consider the top 3 similar users
    df = df.T
    # similarity = similarity.T
    # get the top 3 similar users
    top3 = similarity[item].sort_values(ascending=False)[1:4]
    print(top3)
    # get the ratings of the top 3 similar users for item
    # df
    top3rating = df.loc[user, top3.index]
    print(top3rating)
    # calculate the predicted rating
    rating = np.dot(top3, top3rating) / sum(top3)
    return rating

predict_rating(df, ussim, 'U3', 'M3')