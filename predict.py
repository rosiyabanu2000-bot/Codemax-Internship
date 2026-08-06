import pickle

# Load model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

# User input
hours = float(input("Enter study hours: "))

# Prediction
prediction = model.predict([[hours]])

print(f"\nPredicted Score: {prediction[0]:.2f}")