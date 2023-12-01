#!/usr/bin/env python
# coding: utf-8

# In[40]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch


# In[84]:


URL1 = "https://www.reddit.com/r/GlobalOffensive/comments/17xfwkp/i_made_a_site_that_allows_you_to_preview_all"
heading1 = URL1.split("/")[-1]
with open(r'Data\processed\sentiment_analysis_1.txt','r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize lists to store Comment and Sentiment data
comments = []
sentiments = []

# Parse the lines and extract Comment and Sentiment
comment = ""
sentiment = ""
for line in lines:
    if line.startswith("Comment:"):
        comment = line[len("Comment:"):].strip()
    elif line.startswith("Sentiment:"):
        sentiment = line[len("Sentiment:"):].strip()
        # Append Comment and Sentiment to the lists
        comments.append(comment)
        sentiments.append(sentiment)

# Create a DataFrame from the lists
sentiment1 = pd.DataFrame({'Comment': comments, 'Sentiment': sentiments})

colors = sns.color_palette("Set3")

sentiment_counts = sentiment1['Sentiment'].value_counts()
# print(sentiment_counts.index)
bars = plt.bar(sentiment_counts.index, sentiment_counts.values, color=colors)
plt.title(heading1)
plt.xlabel('Sentiments')
plt.ylabel('Count')

legend_handles = [Patch(color=color, label=sentiment) for sentiment, color in zip(sentiment_counts.index, colors)]

# Add the legend with handles
plt.legend(handles=legend_handles, title='Sentiments', loc='upper right')
plt.xticks(rotation=45)
# Display the plot
plt.savefig('Data\processed\SentimentPlot1.png')


# In[83]:


URL2 = "https://www.reddit.com/r/apple/comments/177xs10/iphone_16_pro_rumor_recap_larger_displays_capture"
heading2 = URL2.split("/")[-1]
# print(heading2)
with open(r'Data\processed\sentiment_analysis_3.txt','r',encoding='utf-8') as file:
    lines = file.readlines()

# Initialize lists to store Comment and Sentiment data
comments = []
sentiments = []

# Parse the lines and extract Comment and Sentiment
comment = ""
sentiment = ""
for line in lines:
    if line.startswith("Comment:"):
        comment = line[len("Comment:"):].strip()
    elif line.startswith("Sentiment:"):
        sentiment = line[len("Sentiment:"):].strip()
        # Append Comment and Sentiment to the lists
        comments.append(comment)
        sentiments.append(sentiment)

# Create a DataFrame from the lists
sentiment2 = pd.DataFrame({'Comment': comments, 'Sentiment': sentiments})

sentiment_counts = sentiment2['Sentiment'].value_counts()
# print(sentiment_counts.index)
bars = plt.bar(sentiment_counts.index, sentiment_counts.values, color=colors)
plt.title(heading2)
plt.xlabel('Sentiments')
plt.ylabel('Count')

legend_handles = [Patch(color=color, label=sentiment) for sentiment, color in zip(sentiment_counts.index, colors)]

# Add the legend with handles
plt.legend(handles=legend_handles, title='Sentiments', loc='upper right')
plt.xticks(rotation=45)
# Display the plot
plt.savefig('Data\processed\SentimentPlot3.png')


# In[81]:


URL3 = "https://www.reddit.com/r/pokemon/comments/loiixy/your_opinion_on_pikachu"
heading3 = URL3.split("/")[-1]
# print(heading3)
with open(r'Data\processed\sentiment_analysis_4.txt','r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize lists to store Comment and Sentiment data
comments = []
sentiments = []

# Parse the lines and extract Comment and Sentiment
comment = ""
sentiment = ""
for line in lines:
    if line.startswith("Comment:"):
        comment = line[len("Comment:"):].strip()
    elif line.startswith("Sentiment:"):
        sentiment = line[len("Sentiment:"):].strip()
        # Append Comment and Sentiment to the lists
        comments.append(comment)
        sentiments.append(sentiment)

# Create a DataFrame from the lists
sentiment3 = pd.DataFrame({'Comment': comments, 'Sentiment': sentiments})

sentiment_counts = sentiment3['Sentiment'].value_counts()
# print(sentiment_counts.index)
bars = plt.bar(sentiment_counts.index, sentiment_counts.values, color=colors)
plt.title(heading3)
plt.xlabel('Sentiments')
plt.ylabel('Count')

legend_handles = [Patch(color=color, label=sentiment) for sentiment, color in zip(sentiment_counts.index, colors)]

# Add the legend with handles
plt.legend(handles=legend_handles, title='Sentiments', loc='upper right')
plt.xticks(rotation=45)
# Display the plot
plt.savefig('Data\processed\SentimentPlot4.png')


# In[79]:


URL4 = "https://www.reddit.com/r/movies/comments/155ag1m/official_discussion_oppenheimer_spoilers"
heading4 = URL4.split("/")[-1]
# print(heading4)
with open(r'Data\processed\sentiment_analysis_5.txt','r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize lists to store Comment and Sentiment data
comments = []
sentiments = []

# Parse the lines and extract Comment and Sentiment
comment = ""
sentiment = ""
for line in lines:
    if line.startswith("Comment:"):
        comment = line[len("Comment:"):].strip()
    elif line.startswith("Sentiment:"):
        sentiment = line[len("Sentiment:"):].strip()
        # Append Comment and Sentiment to the lists
        comments.append(comment)
        sentiments.append(sentiment)

# Create a DataFrame from the lists
sentiment4 = pd.DataFrame({'Comment': comments, 'Sentiment': sentiments})

sentiment_counts = sentiment4['Sentiment'].value_counts()
# print(sentiment_counts.index)
bars = plt.bar(sentiment_counts.index, sentiment_counts.values, color=colors)
plt.title(heading4)
plt.xlabel('Sentiments')
plt.ylabel('Count')

legend_handles = [Patch(color=color, label=sentiment) for sentiment, color in zip(sentiment_counts.index, colors)]

# Add the legend with handles
plt.legend(handles=legend_handles, title='Sentiments', loc='upper right')
plt.xticks(rotation=45)
# Display the plot
plt.savefig('Data\processed\SentimentPlot5.png')


# In[77]:


URL5 = "https://www.reddit.com/r/GlobalOffensive/comments/17xfwkp/i_made_a_site_that_allows_you_to_preview_all"
heading5 = URL5.split("/")[-1]
# print(heading5)
with open(r'Data\processed\sentiment_analysis_2.txt','r', encoding='utf-8') as file:
    lines = file.readlines()

# Initialize lists to store Comment and Sentiment data
comments = []
sentiments = []

# Parse the lines and extract Comment and Sentiment
comment = ""
sentiment = ""
for line in lines:
    if line.startswith("Comment:"):
        comment = line[len("Comment:"):].strip()
    elif line.startswith("Sentiment:"):
        sentiment = line[len("Sentiment:"):].strip()
        # Append Comment and Sentiment to the lists
        comments.append(comment)
        sentiments.append(sentiment)

# Create a DataFrame from the lists
sentiment5 = pd.DataFrame({'Comment': comments, 'Sentiment': sentiments})

colors = sns.color_palette("Set3")

sentiment_counts = sentiment5['Sentiment'].value_counts()
# print(sentiment_counts.index)
bars = plt.bar(sentiment_counts.index, sentiment_counts.values, color=colors)
plt.title(heading5)
plt.xlabel('Sentiments')
plt.ylabel('Count')

legend_handles = [Patch(color=color, label=sentiment) for sentiment, color in zip(sentiment_counts.index, colors)]

# Add the legend with handles
plt.legend(handles=legend_handles, title='Sentiments', loc='upper right')
plt.xticks(rotation=45)
# Display the plot
plt.savefig('Data\processed\SentimentPlot2.png')

