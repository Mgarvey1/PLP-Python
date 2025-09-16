
# ------------------------------
# Import necessary libraries
# ------------------------------
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns  # optional for nicer plots

# ------------------------------
# Task 1: Load and Explore Dataset
# ------------------------------

# Try to load dataset safely
try:
    # Example dataset: Iris dataset (comes with seaborn)
    df = sns.load_dataset("iris")  # Replace with pd.read_csv("your_file.csv") for a local CSV

    print("\n✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: File not found. Make sure the CSV file path is correct.")
    exit()

# Display first few rows
print("🔎 First 5 rows of dataset:")
print(df.head())

# Dataset info
print("\n📊 Dataset Info:")
print(df.info())

# Check for missing values
print("\n❔ Missing Values per Column:")
print(df.isnull().sum())

# Drop rows with missing values (if any)
df = df.dropna()

# ------------------------------
# Task 2: Basic Data Analysis
# ------------------------------

# Summary statistics
print("\n📈 Basic Statistics:")
print(df.describe())

# Grouping: Average petal_length by species
print("\n🌸 Average Petal Length by Species:")
print(df.groupby("species")["petal_length"].mean())

# ------------------------------
# Task 3: Data Visualization
# ------------------------------

# 1. Line chart (not ideal for Iris, but we’ll show sepal_length trend for first 50 samples)
plt.figure(figsize=(8,5))
plt.plot(df["sepal_length"][:50], marker="o")
plt.title("Sepal Length Trend (First 50 Samples)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.show()

# 2. Bar chart - average petal length by species
plt.figure(figsize=(8,5))
df.groupby("species")["petal_length"].mean().plot(kind="bar", color=["#4CAF50","#FF9800","#2196F3"])
plt.title("Average Petal Length by Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(8,5))
plt.hist(df["sepal_width"], bins=15, color="skyblue", edgecolor="black")
plt.title("Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - Sepal length vs. Petal length
plt.figure(figsize=(8,5))
sns.scatterplot(x="sepal_length", y="petal_length", hue="species", data=df, palette="deep")
plt.title("Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# ------------------------------
# Findings
# ------------------------------
print("\n📌 Observations:")
print("1. The Iris dataset has 3 species: Setosa, Versicolor, Virginica.")
print("2. Setosa tends to have smaller petal lengths, while Virginica has the largest.")
print("3. Sepal width is normally distributed, clustering around ~3 cm.")
print("4. Scatter plot shows clear separation of species based on petal/sepal sizes.")
