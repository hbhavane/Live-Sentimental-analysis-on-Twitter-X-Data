import streamlit as st
import warnings
warnings.filterwarnings("ignore")
import pandas as pd
import numpy as np
import tweepy
import re
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
import time
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# To Hide Warnings
st.set_option('deprecation.showfileUploaderEncoding', False)
st.set_option('deprecation.showPyplotGlobalUse', False)

def main():
    st.set_page_config(page_title="LIVE Tweets Sentimental Analysis", layout="wide")
    
    with st.container():
        st.write("")
        st.title("Live Sentimental analysis on Twitter(X) Data")

    with st.container():
        st.write("")
        left_column, right_column = st.columns(2)
        with left_column:
            st.header("\n\n What it actually is??")
            st.write("Live Sentiment Analysis on Twitter(X) Data is a web application designed to analyze the sentiment of tweets related to various topics, focusing on real-time data sourced from Twitter. The application leverages natural language processing (NLP) techniques to determine whether tweets are positive, negative, or neutral in sentiment. Users can input a topic of interest, and the application retrieves tweets using the Twitter API. \n\n")

        image = Image.open('senti2.jpeg')
        st.image(image, caption='Image Generated by AI (deepai.org)', width=600)

    with st.container():
        st.write("")
        st.header("Type Keyword to Get Analysis on Sentiment")

    consumer_key = "lEg4Al8oJzIrSLWeTTPezyGwe"
    consumer_secret = "v5DgsBk4q0M8J1L163dNTnYJpqpSihHX07DlUq2TMA9JVTaJpK"
    access_token = "622799929-slidVIpn7MmtSMl7PyG6vKFC4iCFdUDaarj2e9Zt"
    access_token_secret = "fW4qoZLdHXiCGpvzV5zfvevqu0c9YKm6z9wBPBaI9leB6"

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    def get_tweets(Topic, Count):
        """
        Fetch tweets based on a topic and count using the Twitter API.
        
        Parameters:
        Topic (str): The keyword or hashtag to search tweets.
        Count (int): The number of tweets to retrieve.

        Returns:
        DataFrame: A dataframe containing tweet details such as date, user, tweet text, likes, retweets, and user location.
        """
        df = pd.DataFrame(columns=["Date", "User", "IsVerified", "Tweet", "Likes", "RT", 'User_location'])
        i = 0
        for tweet in tweepy.Cursor(api.search_tweets, q=Topic, count=100, lang="en", exclude='retweets').items():
            time.sleep(0.1)
            df.loc[i, "User"] = tweet.user.name
            df.loc[i, "IsVerified"] = tweet.user.verified
            df.loc[i, "Tweet"] = tweet.text
            df.loc[i, "Likes"] = tweet.favorite_count
            df.loc[i, "RT"] = tweet.retweet_count
            df.loc[i, "User_location"] = tweet.user.location
            df.to_csv("TweetDataset.csv", index=False)
            df.to_excel('{}.xlsx'.format("TweetDataset"), index=False)
            i = i + 1
            if i > Count:
                break
        return df

    def clean_tweet(tweet):
        return ' '.join(re.sub('(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)|([RT])', ' ', tweet.lower()).split())

    def analyze_sentiment(tweet):
        analysis = TextBlob(tweet)
        if analysis.sentiment.polarity > 0:
            return 'Positive'
        elif analysis.sentiment.polarity == 0:
            return 'Neutral'
        else:
            return 'Negative'

    def prepCloud(Topic_text, Topic):
        Topic = str(Topic).lower()
        Topic = ' '.join(re.sub('([^0-9A-Za-z \t])', ' ', Topic).split())
        Topic = re.split("\s+", str(Topic))
        stopwords = set(STOPWORDS)
        stopwords.update(Topic)
        text_new = " ".join([txt for txt in Topic_text.split() if txt not in stopwords])
        return text_new

    def process_data(df, topic):
        df['clean_tweet'] = df['Tweet'].apply(lambda x: clean_tweet(x))
        df["Sentiment"] = df["Tweet"].apply(lambda x: analyze_sentiment(x))

        st.write("Total Tweets Extracted for Topic '{}' are : {}".format(topic, len(df.Tweet)))
        st.write("Total Positive Tweets are : {}".format(len(df[df["Sentiment"] == "Positive"])))
        st.write("Total Negative Tweets are : {}".format(len(df[df["Sentiment"] == "Negative"])))
        st.write("Total Neutral Tweets are : {}".format(len(df[df["Sentiment"] == "Neutral"])))

        return df

    Topic = str(st.text_input("Enter the topic you are interested in (Press Enter once done)"))

    if Topic:
        st.warning("Due to limited access to the Twitter API, we cannot retrieve tweets at this time. We have noted your keyword and will add the data to the topics below soon. Thank you!")
        st.warning(" Please Reload the page and try again from below Topics")
    
    st.header("Use the existing downloaded data from the topics below.")
    

    if st.button("ChatGPT"):
        df = pd.read_csv("TweetDataset2.csv")
        st.session_state['df'] = df
        st.session_state['topic'] = "ChatGPT"

    if st.button("LGBTQ"):
        df = pd.read_csv("TweetDataset2.csv")
        st.session_state['df'] = df
        st.session_state['topic'] = "LGBTQ"
    
    if st.button("Covid Learning"):
        df = pd.read_csv("TweetDataset.csv")
        st.session_state['df'] = df
        st.session_state['topic'] = "Covid Learning"


    if len(Topic) > 0 and not st.session_state.get('df'):
        with st.spinner("Please wait, Tweets are being extracted"):
            df = get_tweets(Topic, Count=200)
        st.success('Tweets have been Extracted !!!!')
        st.session_state['df'] = df
        st.session_state['topic'] = Topic

    if st.session_state.get('df') is not None:
        df = st.session_state['df']
        topic = st.session_state['topic']
        df = process_data(df, topic)

        if st.button("See the Extracted Data"):
            st.success("Below is the Extracted Data :")
            st.write(df.head(50))

        if st.button("Get Count Plot for Different Sentiments"):
            st.success("Generating A Count Plot")
            st.subheader("Count Plot for Different Sentiments")
            plt.figure(figsize=(10, 5))
            sns.countplot(data=df, x="Sentiment")
            st.pyplot()

        if st.button("Get Pie Chart for Different Sentiments"):
            st.success("Generating A Pie Chart")
            a = len(df[df["Sentiment"] == "Positive"])
            b = len(df[df["Sentiment"] == "Negative"])
            c = len(df[df["Sentiment"] == "Neutral"])
            d = np.array([a, b, c])
            explode = (0.1, 0.0, 0.1)
            plt.figure(figsize=(4, 4))  # Adjusted size for better visibility
            patches, texts, autotexts = plt.pie(d, shadow=True, explode=explode, labels=["Positive", "Negative", "Neutral"], autopct='%1.2f%%')
            # Adjust the font size of text and autotexts based on the figure size
            for text in texts:
                 text.set_fontsize(10)  # Set the font size for labels
            for autotext in autotexts:
                 autotext.set_fontsize(10)  # Set the font size for autopct
            st.pyplot()

         
        if st.button("Get Count Plot Based on Verified and unverified Users"):
            st.success("Generating A Count Plot (Verified and unverified Users)")
            st.subheader("Count Plot for Different Sentiments for Verified and unverified Users")
            plt.figure(figsize=(10, 5))
            sns.countplot(data=df, x="Sentiment", hue="IsVerified")
            st.pyplot()

        if st.button("Get WordCloud for all things said about {}".format(topic)):
            st.success("Generating A WordCloud for all things said about {}".format(topic))
            text = " ".join(review for review in df.clean_tweet)
            stopwords = set(STOPWORDS)
            text_newALL = prepCloud(text, topic)
            wordcloud = WordCloud(stopwords=stopwords, max_words=800, max_font_size=50).generate(text_newALL)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            st.pyplot()

        if st.button("Get WordCloud for all Positive Tweets about {}".format(topic)):
            st.success("Generating A WordCloud for all Positive Tweets about {}".format(topic))
            text_positive = " ".join(review for review in df[df["Sentiment"] == "Positive"].clean_tweet)
            stopwords = set(STOPWORDS)
            text_new_positive = prepCloud(text_positive, topic)
            wordcloud = WordCloud(stopwords=stopwords, max_words=800, max_font_size=50).generate(text_new_positive)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            st.pyplot()

        if st.button("Get WordCloud for all Negative Tweets about {}".format(topic)):
            st.success("Generating A WordCloud for all Negative Tweets about {}".format(topic))
            text_negative = " ".join(review for review in df[df["Sentiment"] == "Negative"].clean_tweet)
            stopwords = set(STOPWORDS)
            text_new_negative = prepCloud(text_negative, topic)
            wordcloud = WordCloud(stopwords=stopwords, max_words=800, max_font_size=50).generate(text_new_negative)
            plt.figure(figsize=(10, 5))
            plt.imshow(wordcloud, interpolation='bilinear')
            plt.axis("off")
            st.pyplot()

    if st.button("Exit"):
        st.balloons()

if __name__ == '__main__':
    main()
