import pandas as pd
from textblob import TextBlob

print("Loading combined data...")
# Load the combined data you just created
df = pd.read_csv("output/combined_youtube_data.csv")

print("Cleaning data...")
# Drop rows with missing values
df = df.dropna()

# Function to get sentiment polarity (returns a value from -1.0 to 1.0)
def get_sentiment(text):
    try:
        return TextBlob(str(text)).sentiment.polarity
    except:
        return 0

print("Calculating sentiment scores for video titles... (This may take a moment)")
# Apply the function to create a new column
df['title_sentiment_score'] = df['title'].apply(get_sentiment)

# Categorize the score into Positive, Negative, or Neutral
df['sentiment_category'] = df['title_sentiment_score'].apply(
    lambda x: 'Positive' if x > 0 else ('Negative' if x < 0 else 'Neutral')
)

print(df[['title', 'sentiment_category']].head())

# Save the final cleaned and analyzed dataset for the SQL/Tableau steps
df.to_csv("output/final_analyzed_data.csv", index=False)
print("Sentiment analysis complete! Saved to output/final_analyzed_data.csv")