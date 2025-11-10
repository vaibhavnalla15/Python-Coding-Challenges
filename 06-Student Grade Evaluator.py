""" Write a Python program that:
1. Stores student data — each student has marks in 3 subjects.
2. Calculates each student’s average score.
3. Classifies students as:

    "Distinction" → average ≥ 85
    "Pass" → 50 ≤ average < 85
    "Fail" → average < 50
4. Prints each student’s name, average score, and grade category. """

# Constraints:-
# Handle any number of students.
# Round averages to 2 decimal places.
# Use loops and conditionals (no built-in grading functions).

students = {
    "Alice": [90, 85, 88],
    "Bob": [60, 70, 65],
    "Charlie": [40, 45, 50]
}

for name, marks in students.items():
    avg = round(sum(marks) / len(marks), 2)
    if avg >= 85:
        grade = "Distinction"
    elif 50 <= avg <= 85:
        grade = "Pass"
    else:
        grade = "Fail"
    print(f"{name}: Avg = {avg}, Grade = {grade}")