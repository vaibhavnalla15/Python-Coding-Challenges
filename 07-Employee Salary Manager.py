""" Work with nested dictionaries, loops, and calculations. """

# You have given employee database:-
# You need to:
# 1. Calculate total compensation (salary + bonus) for each employee.
# 2. Print each employee’s total.
# 3. Find and print the highest paid employee with their total compensation.

employees = {
    "John": {"salary": 50000, "bonus": 5000},
    "Emma": {"salary": 60000, "bonus": 8000},
    "Liam": {"salary": 55000, "bonus": 7000}
}

for key, value in employees.items():
    total_comp = value["salary"] + value["bonus"]
    print(f"{key}: {total_comp}")

highest = max(employees, key=lambda name: employees[name]["salary"] + employees[name]["bonus"])
highest_total = employees[highest]["salary"] + employees[highest]["bonus"]

print(f"Highest Paid: {highest} ({highest_total})")

