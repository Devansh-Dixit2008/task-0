"""
Q6. Visualizing the Data with Matplotlib
Uses the PROCESSED csv produced by q5.py (includes the Improvement column).
"""

import pandas as pd
import matplotlib.pyplot as plt


def main():
    df = pd.read_csv("data/processed_student_performance.csv")

    # 1. Bar chart: Student names vs final scores.
    # With 80 students, a full bar chart would be unreadable, so we plot
    # the top 15 by Final_Score to keep labels legible.
    top15 = df.sort_values(by="Final_Score", ascending=False).head(15)
    plt.figure(figsize=(10, 6))
    plt.bar(top15["Student"], top15["Final_Score"], color="steelblue")
    plt.title("Top 15 Students by Final Score")
    plt.xlabel("Student")
    plt.ylabel("Final Score")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig("plots/final_scores.png")
    plt.close()

    # 2. Scatter plot: Hours studied vs final score.
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Hours_Studied"], df["Final_Score"], color="darkorange", alpha=0.7)
    plt.title("Hours Studied vs Final Score")
    plt.xlabel("Hours Studied")
    plt.ylabel("Final Score")
    plt.tight_layout()
    plt.savefig("plots/study_vs_score.png")
    plt.close()

    # 3. Histogram: Distribution of final scores.
    plt.figure(figsize=(8, 6))
    plt.hist(df["Final_Score"], bins=10, color="mediumseagreen", edgecolor="black")
    plt.title("Distribution of Final Scores")
    plt.xlabel("Final Score")
    plt.ylabel("Number of Students")
    plt.tight_layout()
    plt.savefig("plots/score_distribution.png")
    plt.close()

    # 4. Custom plot: Attendance vs Improvement.
    # Interesting question this raises: does higher attendance correlate
    # with a bigger jump from Previous_Score to Final_Score?
    plt.figure(figsize=(8, 6))
    plt.scatter(df["Attendance"], df["Improvement"], color="mediumpurple", alpha=0.7)
    plt.axhline(0, color="gray", linewidth=1, linestyle="--")
    plt.title("Attendance vs Improvement (Final - Previous Score)")
    plt.xlabel("Attendance (%)")
    plt.ylabel("Improvement")
    plt.tight_layout()
    plt.savefig("plots/custom_plot.png")
    plt.close()

    print("Saved: final_scores.png, study_vs_score.png, score_distribution.png, custom_plot.png")


if __name__ == "__main__":
    main()
