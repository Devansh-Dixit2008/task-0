"""
Q5. Pandas and CSV Analysis
"""

import pandas as pd


def main():
    # 1. Load the CSV into a DataFrame.
    df = pd.read_csv("data/student_performance.csv")

    # 2. First five rows.
    print("First 5 rows:")
    print(df.head())

    # 3. Number of rows and columns.
    rows, cols = df.shape
    print(f"\nRows: {rows}, Columns: {cols}")

    # 4. Column names.
    print("\nColumn names:", list(df.columns))

    # 5. Check for missing values (per column, then a single overall flag).
    print("\nMissing values per column:")
    print(df.isnull().sum())
    print("Any missing values at all:", df.isnull().values.any())

    # 6. Average Final_Score.
    print("\nAverage Final_Score:", df["Final_Score"].mean())

    # 7. Student with the highest Final_Score.
    top_student = df.loc[df["Final_Score"].idxmax()]
    print("\nTop student:")
    print(top_student)

    # 8. New column: Improvement.
    df["Improvement"] = df["Final_Score"] - df["Previous_Score"]

    # 9. Students with attendance >= 80 (Boolean mask, same idea as NumPy).
    high_attendance = df[df["Attendance"] >= 80]
    print("\nStudents with Attendance >= 80:")
    print(high_attendance)

    # 10. Sort by Final_Score descending.
    df_sorted = df.sort_values(by="Final_Score", ascending=False)
    print("\nSorted by Final_Score (descending):")
    print(df_sorted.head())

    # 11. Save the processed DataFrame. We keep the ORIGINAL csv untouched
    # and write this sorted, enriched version to a new file.
    df_sorted.to_csv("data/processed_student_performance.csv", index=False)
    print("\nSaved processed_student_performance.csv")


if __name__ == "__main__":
    main()
