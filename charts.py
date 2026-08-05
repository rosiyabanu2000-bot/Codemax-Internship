import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("student_data.csv")

# Bar Chart
plt.bar(data["Name"], data["Math"])
plt.title("Math Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Line Chart
plt.plot(data["Name"], data["Science"], marker="o")
plt.title("Science Scores")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

# Pie Chart
total_marks = data[["Math", "Science", "English"]].sum()

plt.pie(
    total_marks,
    labels=total_marks.index,
    autopct="%1.1f%%"
)
plt.title("Subject-wise Total Marks")
plt.show()