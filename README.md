# Live-Sentimental-analysis-on-Twitter-X-Data
Check out- https://live-sentimental-analysis-harshal-bhavane.streamlit.app/

## What it actually is??
Live Sentiment Analysis on Twitter(X) Data is a web application designed to analyze the sentiment of tweets related to various topics, focusing on real-time data sourced from Twitter. The application leverages natural language processing (NLP) techniques to determine whether tweets are positive, negative, or neutral in sentiment. Users can input a topic of interest, and the application retrieves tweets using the Twitter API. 


![image](https://github.com/hbhavane/Live-Sentimental-analysis-on-Twitter-X-Data/assets/78750775/6e7f4444-5a75-4d1c-9082-76e0d64f17b9)

## Functionality Overview:

#### Topic Input: 
Users can enter a keyword or topic of interest related to tweets they want to analyze.

#### Data Extraction:
  The application fetches tweets in real-time using the Twitter API based on the entered topic. It also supports analysis on pre-downloaded datasets related to specific topics like "Covid Learning" and "LGBTQ (no added yet)".

#### Sentiment Analysis:
  Each tweet's sentiment (positive, negative, neutral) is determined using TextBlob, a Python library for processing textual data.

#### Visualization:
- Extracted Data Display: Displays a preview of the extracted tweets with details such as user name, tweet content, sentiment, etc.
![image](https://github.com/hbhavane/Live-Sentimental-analysis-on-Twitter-X-Data/assets/78750775/ae185a82-d154-4224-811d-64728b2517cf)

- Count Plot: Generates a count plot showing the distribution of sentiments (positive, negative, neutral) among the extracted tweets.
![image](https://github.com/hbhavane/Live-Sentimental-analysis-on-Twitter-X-Data/assets/78750775/b0b094b4-3a80-4082-9bf3-fb56406c4ab9)

- Pie Chart: Displays a pie chart illustrating the proportion of positive, negative, and neutral sentiments in the dataset.
![image](https://github.com/hbhavane/Live-Sentimental-analysis-on-Twitter-X-Data/assets/78750775/1ce9e8c9-e324-4741-aaf6-da08522f4671)

- Count Plot by Verified Status: Generates a count plot comparing sentiment distribution among verified and unverified Twitter users.
![image](https://github.com/hbhavane/Live-Sentimental-analysis-on-Twitter-X-Data/assets/78750775/42587a90-dda9-44c7-b9c9-5604b2581335)


- WordCloud: Generates a word cloud visualizing the most frequent words used in tweets related to the analyzed topic.
![image](https://github.com/hbhavane/Live-Sentimental-analysis-on-Twitter-X-Data/assets/78750775/0959814a-79f4-4f7c-8b52-43dd681fbd56)

#### Data Export: 
Provides an option to download the extracted tweet data as a CSV file for further analysis.


## Purpose
The purpose of this application is to provide users with insights into public sentiment on Twitter regarding specific topics. It serves as a tool for social media monitoring, brand sentiment analysis, and understanding public opinion dynamics in real-time.


