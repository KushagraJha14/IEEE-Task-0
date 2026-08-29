import pandas as pd

df = pd.read_csv("data/student_performance.csv")

print(df.head())
print(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")
print(list(df.columns))
print(df.isnull().sum())

print(f"Average Final Score: {df['Final_Score'].mean()}")

top_student = df.loc[df["Final_Score"].idxmax(), "Student"]
print(f"Top Student: {top_student}")

df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

print(df[df["Attendance"] >= 80])

df_sorted = df.sort_values(by="Final_Score", ascending=False)
df_sorted.to_csv("data/processed_student_performance.csv", index=False)