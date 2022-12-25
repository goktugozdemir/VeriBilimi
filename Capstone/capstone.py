# -*- coding: utf-8 -*-
"""Capstone

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13e3VbrG2qoCSiHI7Ljzg2IUTHWtxAlXZ

#  Predicting İmdb Scores of Tv Shows and Movies in Netflix

Ahmet Göktuğ Özdemir

Capstone Project

December 2022

# Table of Contents


*   Summary
*   Motivation
* Literature Review
* Data Exploration & Codes
* Results
*   Referances

# Summary

This project aims to make a algorithm that can predict a tv show or movies imdb score and if entry will get higher score than median score.The Internet Movie Database (IMDb) is an online database containing information and statistics about movies, TV shows and video games as well as actors, directors and other film industry professionals. İn this project dataset(1) was used which has all movies and tv shows from Netflix up to year 2021. Netflix is one of the most popular media and video streaming platforms. They have over 8000 movies or tv shows available on their platform, currently they have over 200M Subscribers globally. Dataset consist of 8807 rows and 12 columns. Project consist of data exploration, dataset preparation, making the algorithm and discussing results. At the moment it uses k-nn algorithm.

# Motivation

Currently Netflix is the biggest streaming service. I wanted to make something that could predict if something is worth my time. I used imdb rating as imdb scores are more reliable indicator of quality than Netflix's own scores. As for the reason I used only Netflix entrys I thought as Netflix is biggest streaming service their catalouge should be better than what is avaible in avarage and should be more known. With this I could know if something is good before it is released. I plan to use it for newly released titles rather than unreleased ones. This way before ratings are made I could decide if I should watch it or not.

# Literature Review

One of the widely used classification algorithms is k-Nearest Neighbours (k-NN). Its popularity is mainly due to its simplicity, effectiveness, ease of implementation and ability to add new data in the training set at any time. However, one of its main drawbacks is the fact that its performance is highly dependent on the proper selection of parameter k, i.e. the number of nearest neighbours that the algorithm examines. The most frequently used technique for the “best” k determination is the cross validation as there is no general rule for choosing the k value due to its dependency on the training dataset. However, selecting a fixed k value throughout the dataset does not take into account its special features, like data distribution, class separation, imbalanced classes, sparse and dense neighborhoods and noisy subspaces(2)

As other researches indicates Netflix data set provides very little data for each movie -- only its title, the ratings
from the users and the date of the ratings -- so we use the Internet Movie Database 
for richer metadata. We also experimented with clustering sparser metadata like actors and
actresses. We then ran experiments on predicting ratings with and without the richer
metadata. We found that enriching that enriching our baseline collaborative filtering
approach with movie metadata only made a small improvement of 0.1% in the root mean
squared error (RMSE) of our predictions(3)

# Data Exploration & Codes
"""

!pip install git+https://github.com/nielth/cinemagoer

"""We import our packages."""

import http.client
import imdb
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from imdb import Cinemagoer
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
import seaborn as sb
import nltk as nl
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, plot_confusion_matrix

def remove_suffix(input_string, suffix):
    if suffix and input_string.endswith(suffix):
        return input_string[:-len(suffix)]
    return input_string

"""Because getting data from imdb api takes too much time I worked with only 100 data for this time. For gettin all data from imdb takes up to 15 hours. By changing nrows we can use more of dataset."""

pd.options.mode.chained_assignment=None

ia = Cinemagoer()

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 1000)
pd.set_option('display.width', 1000)

df = pd.read_csv("netflix_titles.csv",nrows=100)
print(df.head())

nullcheck=df.isnull()

"""Showing null entry numbers."""

print(df.isna().sum())

y=df.isna().sum()
x =df.columns
f = plt.figure()
f.set_figwidth(15)
f.set_figheight(3)
print()
plt.bar(x,y)
plt.title('Number of Null Values')
plt.show()

"""Getting missing values from imdb with cinemagoer api from imdb."""

for i in range(len((nullcheck["director"]))):
    if (((nullcheck["director"][i])==True)):
        try:
            movies = ia.search_movie(df["title"][i])
            if (len(movies)>0):
                movieid = movies[0].movieID
                truemovie = ia.get_movie(movieid)
                director = []
                print(i)
                for j in range(len(truemovie["directors"])):
                    director.append(truemovie["directors"][j]["name"])
            else:
                print("Film does not exist in imdb")
        except KeyError:
                    print("No director entry in imdb")
                    if(df["type"][i]=="TV Show"):
                        print("It is a Tv Show")
                        director.append("Tv Show")
        except imdb._exceptions.IMDbParserError:
                    print("Invalid title")
        except imdb._exceptions.IMDbDataAccessError:
                    print("Timed out")
                    i = i - 1
        except http.client.IncompleteRead:
                    print("Incomplete Read")
                    i = i - 1
        s = ','.join(director)
        df.iloc[:, 3][i] = s

for i in range(len((nullcheck["country"]))):
    if (((nullcheck["country"][i])==True)):
        try:
            movies = ia.search_movie(df["title"][i])
            if (len(movies)>0):
                movieid = movies[0].movieID
                truemovie = ia.get_movie(movieid)
                country = []
                print(i)
                for j in range(len(truemovie["countries"])):
                    country.append(truemovie["countries"][j])
            else:
                print("Film does not exist in imdb")
            s = ','.join(country)
            df.iloc[:, 5][i] = s
        except KeyError:
                    print("No country entry in imdb")
        except imdb._exceptions.IMDbParserError:
                    print("Invalid title")
        except imdb._exceptions.IMDbDataAccessError:
                    print("Timed out")
                    i = i - 1
        except http.client.IncompleteRead:
                    print("Incomplete Read")
                    i = i - 1

df.to_csv('complete_netflix_data.csv')
for i in range(len(df["cast"])):
    try:
        if (nullcheck["cast"][i])==True:
            movies = ia.search_movie(df["title"][i])
            if (len(movies)>0):
                movieid = movies[0].movieID
                truemovie = ia.get_movie(movieid)
                cast=[]
                print(i)
                for j in range(len(truemovie["cast"])):
                    cast.append(truemovie["cast"][j]["name"])
            else:
                print("Film does not exist in imdb")
            s = ','.join(cast)
            df.iloc[:, 4][i] = s
    except KeyError:
                print("No cast entry in imdb")
    except imdb._exceptions.IMDbParserError:
            print("Invalid title")
    except imdb._exceptions.IMDbDataAccessError:
            print("Timed out")
            i = i - 1
    except http.client.IncompleteRead:
            print("Incompleted Read")
            i = i - 1
df.to_csv('complete_netflix_data.csv')

score = []
for i in range(len((df["director"]))):
        try:
            movies = ia.search_movie(df["title"][i])
            if (len(movies)>0):
                movieid = movies[0].movieID
                truemovie = ia.get_movie(movieid)
                print(i)
                score.append(truemovie["rating"])
            else:
                print("Film does not exist in imdb")
                score.append(None)
        except KeyError:
                    print("No rating entry in imdb")
                    score.append(None)
        except imdb._exceptions.IMDbParserError:
                    print("Invalid title")
        except imdb._exceptions.IMDbDataAccessError:
                    print("Timed out")
                    i = i - 1
        except http.client.IncompleteRead:
                    print("Incomplete Read")
                    i = i - 1


df["Score"] = score

"""Showing remaining null values and dropping ones that could not be filled."""

print("Null entry number:")
print(df.isna().sum())
print()
print("Drop null entrys")
df.dropna(inplace=True)

df.to_csv('complete_netflix_data.csv')

print(df.head())
print()
print()
print("Null entry number:")
print(df.isna().sum())
print()

"""Showing column types."""

print(df.info())

print(df.describe())

y=df.isna().sum()
print()
x =df.columns
f = plt.figure()
f.set_figwidth(15)
f.set_figheight(3)
plt.bar(x,y)
plt.title('Number of Nan Values')
plt.show()
print()
print()

"""As we can see Netflix has more movies than Tv shows."""

graph = [df['type'].value_counts()['Movie'], df['type'].value_counts()['TV Show']]
label = ["Movies", "Tv Shows"]
y = graph
plt.pie(y, labels=label,autopct='%1.1f%%',shadow=True, startangle=90)
plt.title('Percentage of Movies and Tv Shows')
plt.show()
print()
print()

"""As seen in graphic united states has the most entrys."""

f = plt.figure()
f.set_figwidth(14)
f.set_figheight(3)
df['country'].value_counts()[:20].plot(kind='barh')
plt.title('Country locations where entry was filmed')
plt.show()

"""Because Tv shows have no director entry in imdb I gave Tv show directors 'Tv Show' label. Because of this there seems to be a lot of tv shows in directors. After that we can see directors with most number of films."""

f = plt.figure()
df['director'].value_counts()[:20].plot(kind='barh')
f.set_figwidth(16)
f.set_figheight(3)
interval = range(0, 22, 2)
plt.xticks(interval)
plt.title('Entry Number by Directors')
plt.show()

"""Below is some histograms of different values."""

graph = df['release_year'].value_counts().plot.bar()
plt.title('Entry Release Years')
plt.show()


print()
print()

plt.hist(df["date_added"])
plt.xticks(rotation = 90)
plt.title('Date Added')
plt.show()

print()
print()

plt.hist(df["Score"])
plt.title('Score')
plt.show()

print()
print()

"""We can see the scores median and means."""

print("Median Score")
print(df["Score"].median())
print("Mean Score")
print(df["Score"].agg('mean'))




df['director']=df['director'].astype('category')
df['country']=df['country'].astype('category')
df['cast']=df['cast'].astype('category')
df['listed_in']=df['listed_in'].astype('category')

df['type']=df['type'].astype('category')
df['rating']=df['rating'].astype('category')
df['release_year']=df['release_year'].astype('category')

"""We use dummies to one hot encode our catagories. Reason we use dummies and not sklearn is we have multiple values in one cell."""

df1 = df['listed_in'].str.get_dummies(',').add_prefix('listed_in_')
df2 = df['country'].str.get_dummies(',').add_prefix('country_')
df3 = df['cast'].str.get_dummies(',').add_prefix('cast_')
df4 = df['director'].str.get_dummies(',').add_prefix('director_')

df=df.drop(['cast','director','listed_in','country'], axis=1)
df = pd.concat([df, df1,df2,df3,df4], axis=1, join='inner')
df

"""Because we have Tv shows and movies in same dataset some values are seasons and some are minutes. We can not work with that so we make all of them categorical by making minutes categorical."""

for i in range(len(df['duration'])):
 try:
  if ('Seasons' in df['duration'][i]):
   print('Passed because its a Tv Show')
  elif('Season' in df['duration'][i]): 
   print('Passed because its a Tv Show')
  else:
    df['duration'][i]=remove_suffix(df['duration'][i],' min')
    print(df['duration'][i])
    number=int(df['duration'][i])
    if(number<70):
     df['duration'][i]='Shorter than a hour and ten minutes'  
    elif(number<150):
     df['duration'][i]='Between one or two and half hour'
    elif(number>120):
     df['duration'][i]='Longer than two and half hour'  
 except(KeyError):
  continue
df['duration']=df['duration'].astype('category')

"""We visualize the change."""

plt.hist(df["duration"])
plt.title('Entry Durations')
plt.xticks(rotation = 90)
plt.show()

"""We use one hot encoding to make other values categorical."""

transformer = make_column_transformer(
    (OneHotEncoder(), ['type','release_year','rating','duration']),remainder='passthrough',sparse_threshold=0)

transformed = transformer.fit_transform(df)
transformed_df = pd.DataFrame(
    transformed, 
    columns=transformer.get_feature_names_out()
)

transformed_df.columns = transformed_df.columns.str.replace("onehotencoder__", " ")

transformed_df.columns = transformed_df.columns.str.replace("remainder__", " ")

"""Because we have too much columns we drop ones with less than 5 occurrence so we can work with our data better."""

vec = CountVectorizer(stop_words='english')
X1 = vec.fit_transform(transformed_df[" title"]) 
count_array = X1.toarray() 
X1 = pd.DataFrame(data=count_array,columns = vec.get_feature_names_out())
for (columnName, columnData) in X1.iteritems():
  if(X1[columnName].sum()<5):
    X1=X1.drop([columnName],axis=1)
transformed_df = pd.concat([transformed_df,X1], axis=1, join='inner') 
transformed_df=transformed_df.drop([' title'],axis=1) 
transformed_df=transformed_df.drop([' date_added'],axis=1) 
transformed_df=transformed_df.drop([' show_id'],axis=1)

"""We tokenize the description and get values which has more than 5 occurrences."""

X2 = vec.fit_transform(transformed_df[" description"]) 
count_array = X2.toarray() 
X2 = pd.DataFrame(data=count_array,columns = vec.get_feature_names_out())
for (columnName, columnData) in X2.iteritems():
  if(X2[columnName].sum()<5):
    X2=X2.drop([columnName],axis=1)
transformed_df = pd.concat([transformed_df,X1], axis=1, join='inner') 
transformed_df=transformed_df.drop([' description'],axis=1)

score=transformed_df[" Score"]
transformed_df=transformed_df.drop([' Score'],axis=1)
transformed_df["score"] = score

for (columnName, columnData) in transformed_df.iteritems():
  if(type(columnData.values[0])==int or type(columnData.values[0])==float):
    if(columnData.values[0]==1 or columnData.values[0]==0):
        if(transformed_df[columnName].value_counts()[1]<5):
          transformed_df=transformed_df.drop([columnName],axis=1)

transformed_df.head()

transformed_df.describe()

"""As we can see we don't have much correlation with anything."""

transformed_df.astype('float64').corr()

"""For us to make classification we need a new column. We make a column of if a entry has higher or lower than median score. """

cl=[]
for i in range(len(transformed_df['score'])):
 try:
  if ( transformed_df['score'][i]>6.5 ):
   cl.append('Higher than median')
  elif(transformed_df['score'][i]<=6.5): 
   cl.append('Lower than median')  
 except(KeyError):
  continue
transformed_df['Class']=cl
transformed_df

"""We use label encoder and train test split to split and prepare our data."""

le = preprocessing.LabelEncoder()
encoded=le.fit_transform(transformed_df['Class'])
transformed_df=transformed_df.drop(['Class'],axis=1)
X_train, X_test, y_train, y_test = train_test_split(transformed_df,encoded,test_size=0.3,random_state=25)

knn = KNeighborsClassifier()
k_range = list(range(1, 31))
param_grid = dict(n_neighbors=k_range)
grid = GridSearchCV(knn, param_grid, cv=10, scoring='accuracy', return_train_score=False,verbose=1)
grid_search=grid.fit(X_train, y_train)

"""As seen our accuracy for classification is high."""

y_test_hat=grid_search.predict(X_test) 

test_accuracy=accuracy_score(y_test,y_test_hat)*100

print("Accuracy for our testing dataset with tuning is : {:.2f}%".format(test_accuracy) )

plot_confusion_matrix(grid,X_train, y_train,values_format='d' )

sb.heatmap(transformed_df.astype('float64').corr())
score = transformed_df['score']
transformed_df=transformed_df.drop(['score'],axis=1)

score=score.astype(int)

X_train, X_test, y_train, y_test = train_test_split(transformed_df, score, random_state = 25,test_size=0.30)
X_train.head()

print(X_test.head())
print()
print()
print(y_train.head())

"""We try to make a regression prediction too."""

scaler = MinMaxScaler(feature_range=(0, 1))
x_train_scaled = scaler.fit_transform(X_train)
x_train = pd.DataFrame(x_train_scaled)

x_test_scaled = scaler.fit_transform(X_test)
x_test = pd.DataFrame(x_test_scaled)

knn = KNeighborsRegressor()
grid_params = { 'n_neighbors' : [5,7,9,11,13,15],
               'weights' : ['uniform','distance'],
               'metric' : ['minkowski','euclidean','manhattan']}
gs = GridSearchCV(knn, grid_params, verbose = 1, cv=3, n_jobs = -1)
g_res = gs.fit(X_train, y_train)

g_res.best_score_

g_res.best_params_

"""As seen our data in current state can not make accurate predictions."""

print(g_res.score(X_test, y_test))
scores = cross_val_score(knn, transformed_df, score, cv =5)
print()
print()
print('Model accuracy: ',np.mean(scores))

"""# Results

As seen from our results we can accurately predict if something is better than avarage but we can not predict precise scores. This means we need a different dataset or columns. 
  We can use this as it is for some predictions and we can select what is worth our time.

# References


1.   https://www.kaggle.com/datasets/shivamb/netflix-shows?resource=download
2.   Dynamic k determination in k-NN classifier: A literature review
3.  Netflix Movie Rating Prediction using Enriched Movie Metadata
"""