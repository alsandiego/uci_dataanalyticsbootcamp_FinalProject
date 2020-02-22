# UCI_DataAnalytics_Bootcamp_FinalProject: Twitter Sentiment Analysis
## Team Members:
- Nurbol Batkhan
- Abigail Fabella
- Rose Militante
- Al San Diego

Github Repo: https://github.com/alsandiego/UCI_Bootcamp_FinalProject

## Project Inspiration:
As humans, we can guess the sentiment of a sentence whether it is positive or negative. Businesses have a need for understanding customer sentiment as people and markets respond to product and business decisions. This enables businesses to:
Predict the outcome of upcoming events.
Evaluate the impact of a recent product launch.
Pivot the direction or content of an ad campaign, and more.

These use cases inspired our group to set forth developing our own simple Twitter Sentiment Analysis via a supervised learning model using python and NLP libraries. 

To further focus our analysis on a specific industry, we created a visualization on sentiment towards common fast food brands.

## Summary:

Using python and NLP libraries we set out to create a machine learning model to apply towards our tweet data of interest. Since we chose the route of using a supervised learning approach, we obtained an existing dataset found on Kaggle put out by Stanford University containing hundreds of lines of tweets with sentiments already classified. This was used to train and test our model.

### NLTK Classifiers Tested: 
Naïve Bayes: Train set: 100k tweets, runtime: 10+ hours, accuracy: 73.26%
Decision Tree: Train set: 1k, accuracy: 61.8%
TypedMaxentFeatureEncoding: Train set: 4k, accuracy: 52%
SKLearn BernoulliNB feature set train set: 25k, accuracy: 74.37%, runtime: 30 mins
SKLearn SVC feature set, train set: 25k, accuracy: 77.99%, runtime: 10+ hours

### Backend Process:
Use Twitter API to pull test data set based on a keyword
Import training and validation data set from CSV files to build the model
Preprocess the dataset using a function (sentence clean up)
Use the NLTK algorithm to build a model that will be used to analyze sentiments
Use the validation data set to get the accuracy of the training model
Use the model that has provided the highest accuracy, SKLearn with the feature set SVC, to compare the test data set
Export the data to CSV for use with the dashboard

A twitter account and application was established to be granted the customer and access keys. Our twitter account could then be connected to python in our Jupyter notebook to extract the required tweets. Using this connection, we are able to extract tweets using a particular keyword or hashtag. For consistency we used just the restaurant names to gather our needed tweet data.

We wanted to include geo mapping to display sentiment location. However, our free twitter API access only provided locations when a user designates it on their profile, not where they actually tweeted from. Locations were inaccurate and misleading as users could designate false places such as “Somewhere, Earth”, “Home”, and “Space”, which is unmappable.

Once we obtained the tweet data, this was converted into a dataframe which makes it more readable and easier to work with. Using the training and test dataset from Sentiment140, we preprocessed it before running it on multiple machine learning algorithms. After finding the best one that provided the highest accuracy, we used Pickle to save the model for later use and testing. The tweets that were downloaded using our API was then compared to the model to analyze the sentiments of the tweet whether it is positive or negative.

### Manipulation of the dataframe was needed for our required column layout: 
* Search_Term – for our use case we were searching for restaurant names 
* Date and time
* Tweet
* Sentiment (Use algorithm to positive/negative sentiment)
* Score (Positive = 1, Negative = -1)

We then proceeded to extract the data into a csv stored in an Amazon Web Services S3 bucket for accessibility. Dash was used to connect the data, filter through it using a Pandas dataframe, perform calculations and visualize our analysis in a responsive dashboard. 

In conclusion, sentiment analysis is a difficult technology to get right. There are many obstacles involved with natural language processing. However, the return when done appropriately has a wide variety of benefits from its results. The insights gained from statements and opinions expressed on social media is vital for many companies’ decision making. 

### Python Modules Used:
python-twitter
OS
config
time
pandas
numpy
re
nltk
string
sklearn
pickle



### Resources:
The basis of our Python Code: https://towardsdatascience.com/creating-the-twitter-sentiment-analysis-program-in-python-with-naive-bayes-classification-672e5589a7ed

Training and Test Dataset for Twitter Sentiment Analysis:
https://www.kaggle.com/kazanova/sentiment140

NLTK Classifiers:
https://www.nltk.org/howto/classify.html

Dash Tutorials:
https://github.com/amyoshino/Dash_Tutorial_Series
