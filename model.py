import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import pickle

# Load dataset
data = pd.read_csv("data/student_scores.csv")

# Features and target
X = data[["Hours"]]
y = data["Score"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Accuracy
accuracy = model.score(X_test, y_test)
print("Model Accuracy:", round(accuracy * 100, 2), "%")

# Save model
with open("student_model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model saved as student_model.pkl")

# Plot
plt.scatter(X, y, color="blue", label="Actual Data")
plt.plot(X, model.predict(X), color="red", label="Regression Line")
plt.xlabel("Study Hours")
plt.ylabel("Score")
plt.title("Student Performance Prediction")
plt.legend()
plt.show()