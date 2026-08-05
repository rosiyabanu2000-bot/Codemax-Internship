import pandas as pd
import numpy as np

# Load dataset
data = pd.read_csv("student_data.csv")

# Display dataset
print("Dataset:")
print(data)

# Basic statistics
print("\nStatistics:")
print(data.describe())

# Average marks
print("\nAverage Marks:")
print(data[["Math", "Science", "English"]].mean())

# Highest Math mark
print("\nHighest Math Score:")
print(data["Math"].max())

# Lowest Science mark
print("\nLowest Science Score:")
print(data["Science"].min())

# Add Total column
data["Total"] = data["Math"] + data["Science"] + data["English"]

print("\nDataset with Total:")
print(data)