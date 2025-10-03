from datasets import load_dataset
import pandas as pd

# Load TripAdvisor review-rating dataset
dataset = load_dataset("jniimi/tripadvisor-review-rating")

# Convert to pandas DataFrame
df = dataset["train"].to_pandas()

print(df.shape)
print(df.columns)
print(df.head())


df.to_csv("data/tripadvisor_aspect_reviews.csv", index=False)
