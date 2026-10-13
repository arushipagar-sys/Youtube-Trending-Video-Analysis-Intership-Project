import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore') # Hides unnecessary warnings

print("Loading data for visualization...")
df = pd.read_csv("output/final_analyzed_data.csv")

print("Formatting dates...")
# Convert trending_date to standard datetime format
df['trending_date'] = pd.to_datetime(df['trending_date'], errors='coerce', format='mixed')

# Remove rows where the date could not be read
df = df.dropna(subset=['trending_date'])

print("Generating Time-Series Visualization...")
# Set the style for the plot
sns.set_theme(style="darkgrid")
plt.figure(figsize=(12, 6))

# Calculate the number of trending videos per day
daily_trends = df.groupby(df['trending_date'].dt.date).size()

# Create the time-series line plot
sns.lineplot(x=daily_trends.index, y=daily_trends.values, color='purple', linewidth=2)

# Customize the chart labels
plt.title('YouTube Trending Activity Over Time', fontsize=16, fontweight='bold')
plt.xlabel('Trending Date', fontsize=12)
plt.ylabel('Number of Trending Videos', fontsize=12)
plt.xticks(rotation=45)
plt.tight_layout()

# Save the chart as an image file
plt.savefig('output/trending_time_series.png')
print("Visualization complete! Saved chart to output/trending_time_series.png")