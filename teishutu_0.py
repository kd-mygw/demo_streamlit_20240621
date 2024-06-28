import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix

st.title("Iris Dataset - Logistic Regression Model")

# Load the dataset
@st.cache
def load_data():
    data = sns.load_dataset('iris')
    return data

data = load_data()

# Show the dataset
st.subheader("Iris Dataset")
st.write(data.head())

# Data visualization
st.subheader("Data Visualization")
st.write("Scatter plot between Sepal Length and Sepal Width")
fig, ax = plt.subplots()
sns.scatterplot(data=data, x="sepal_length", y="sepal_width", hue="species", ax=ax)
st.pyplot(fig)

# Select features and target
X = data[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
y = data['species']

# Split the data
st.subheader("Model Training and Evaluation")
test_size = st.slider("Test Size (percentage)", 10, 50, 20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size/100, random_state=42)

# Train the model
model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Model evaluation
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)

st.write(f"Accuracy: {accuracy:.2f}")

st.write("Confusion Matrix")
fig, ax = plt.subplots()
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', ax=ax, xticklabels=model.classes_, yticklabels=model.classes_)
plt.xlabel('Predicted')
plt.ylabel('Actual')
st.pyplot(fig)

if st.button('Show Detailed Metrics'):
    from sklearn.metrics import classification_report
    report = classification_report(y_test, y_pred, target_names=model.classes_)
    st.text(report)
