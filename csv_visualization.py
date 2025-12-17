import pandas as pd
import matplotlib.pyplot as plt

# Load CSV data
data = pd.read_csv("students_marks.csv")

print(data)

plt.plot(data["Name"], data["Marks"], marker='o')

plt.title("Student Marks Trend")
plt.xlabel("Student Name")
plt.ylabel("Marks")
plt.grid(True)

plt.show()



plt.bar(data["Name"], data["Marks"])

plt.title("Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()



plt.scatter(data["Hours_Studied"], data["Marks"])

plt.title("Hours Studied vs Marks")
plt.xlabel("Hours Studied")
plt.ylabel("Marks")

plt.show()


