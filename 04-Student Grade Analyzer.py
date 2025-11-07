""" Write a Python program that takes multiple students’ marks and outputs:
- Each student’s average score
- The highest-scoring student """

# Input: Dictionary where keys are student names and values are lists of marks.
# Constraints:
# Assume each student has at least one score.
# Round averages to 2 decimal places.

info = {
    "Alice": [80, 90, 85],
    "Bob": [70, 85, 80],
    "Charlie": [90, 95, 90] }

avg_scores = {name: round(sum(marks)/len(marks), 2) for name, marks in info.items()}
for key, value in avg_scores.items():
    print(key,":",value)

top_student = max(avg_scores, key=avg_scores.get)
print("Top student:",top_student)

