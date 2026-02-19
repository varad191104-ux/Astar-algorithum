import pandas as pd
import numpy as np

academic_data = pd.DataFrame({
    "StudentID": [1, 2, 3, 4, 5, 3],
    "Name": ["Rahul", "Priya", "Amit", "Sneha", "Rohan", "Amit"],
    "Math": [78, 85, np.nan, 90, 88, np.nan],
    "Science": [80, np.nan, 75, 92, 89, 75],
    "English": [70, 88, 72, np.nan, 85, 72]
})

attendance_data = pd.DataFrame({
    "StudentID": [1, 2, 3, 4, 5],
    "Attendance": [85, 90, np.nan, 95, 88]
})

df = academic_data.copy()
df = df.sort_values("Name")
df = df.drop_duplicates()

df["Math"] = df["Math"].fillna(df["Math"].mean())
df["Science"] = df["Science"].fillna(df["Science"].mean())
df["English"] = df["English"].fillna(df["English"].mean())

df = df[df["Math"] > 80]

df = pd.merge(df, attendance_data, on="StudentID", how="left")
df["Attendance"] = df["Attendance"].fillna(df["Attendance"].mean())

print(df.select_dtypes(include=np.number).mean())
print(df.select_dtypes(include=np.number).median())
print(df.select_dtypes(include=np.number).std())

for col in ["Math", "Science", "English", "Attendance"]:
    df[col] = (df[col] - df[col].min()) / (df[col].max() - df[col].min())

    df[col] = (df[col] - df[col].mean()) / df[col].std()


df = df.drop("Name", axis=1)
df.to_csv("student_final_data.csv", index=False)