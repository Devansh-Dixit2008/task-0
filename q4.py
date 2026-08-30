"""
Q4. NumPy Basics
Values are hardcoded here (mirroring the first several rows of the dataset)
-- we are NOT reading the CSV in this question, per the instructions.
"""

import numpy as np


def main():
    hours_studied = np.array([5.9, 3.6, 6.5, 5.4, 1.2, 7.3, 5.8, 6.0, 1.4, 3.7])
    attendance = np.array([100, 85, 73, 73, 74, 92, 69, 62, 70, 56])
    previous_scores = np.array([52, 74, 49, 78, 77, 49, 83, 66, 85, 47])
    final_scores = np.array([60, 47, 41, 50, 35, 69, 53, 55, 36, 36])

    # 1. Shape and dtype of each array.
    for name, arr in [
        ("hours_studied", hours_studied),
        ("attendance", attendance),
        ("previous_scores", previous_scores),
        ("final_scores", final_scores),
    ]:
        print(f"{name}: shape={arr.shape}, dtype={arr.dtype}")

    # 2-4. Mean, max, min, std -- all vectorized NumPy reductions, no manual loops.
    print("Mean final score:", final_scores.mean())
    print("Max final score:", final_scores.max())
    print("Min final score:", final_scores.min())
    print("Std dev of final scores:", final_scores.std())

    # 5. Add 5 bonus marks to every score in one vectorized operation.
    bonus_scores = final_scores + 5
    print("Scores with +5 bonus:", bonus_scores)

    # 6. Boolean array: True where a student scored >= 75.
    passed_75 = bonus_scores >= 75
    print("Scored >= 75 (boolean mask):", passed_75)

    # 7. Boolean indexing: use the mask itself as an index to filter the array.
    print("Scores >= 75:", bonus_scores[passed_75])


if __name__ == "__main__":
    main()
