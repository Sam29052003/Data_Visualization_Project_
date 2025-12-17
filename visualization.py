# Step 1: Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 2: Load dataset
data = pd.read_csv("students.csv")

# Set Seaborn style
sns.set(style="whitegrid")


# CHART 1: Trend - Average Scores
average_scores = data[['Math', 'Science', 'English']].mean()

plt.figure()
average_scores.plot(kind='line', marker='o')
plt.title("Average Scores by Subject")
plt.xlabel("Subject")
plt.ylabel("Average Score")
plt.show()



# CHART 2: Relationship - Math vs Science
plt.figure()
sns.scatterplot(x='Math', y='Science', data=data)
plt.title("Math vs Science Relationship")
plt.xlabel("Math Score")
plt.ylabel("Science Score")
plt.show()



# CHART 3: Comparison - Attendance
plt.figure()
sns.barplot(x='Name', y='Attendance', data=data)
plt.title("Student Attendance Percentage")
plt.xticks(rotation=45)
plt.show()



# CHART 4: Outliers - Score Distribution
plt.figure()
sns.boxplot(data=data[['Math', 'Science', 'English']])
plt.title("Score Distribution & Outliers")
plt.ylabel("Scores")
plt.show()