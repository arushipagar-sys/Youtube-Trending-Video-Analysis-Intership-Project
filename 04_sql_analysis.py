import pandas as pd
import sqlite3

print("Loading final analyzed data...")
df = pd.read_csv("output/final_analyzed_data.csv")

print("Setting up SQL database...")
# Create a temporary database in your computer's memory
conn = sqlite3.connect(':memory:') 

# Load the dataframe into the SQL database as a table named 'youtube_data'
df.to_sql('youtube_data', conn, index=False)

print("Running SQL Query to rank categories by average views...\n")
# Write your SQL query 
sql_query = """
SELECT category_id, ROUND(AVG(views), 0) AS avg_views
FROM youtube_data
GROUP BY category_id
ORDER BY avg_views DESC
"""

# Execute the query and store the results
top_categories = pd.read_sql(sql_query, conn)

print("Top Categories by Average Views:")
print(top_categories.head(10))

# Save these SQL results to a new CSV so you can use them in your Tableau Dashboard
top_categories.to_csv("output/sql_category_rankings.csv", index=False)
print("\nSQL results saved successfully to output/sql_category_rankings.csv!")