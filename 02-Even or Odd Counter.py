""" Write a program that takes a list of numbers from the user and counts how many are even and how many are odd. """

user_input = input("Enter comma-separated list (e.g., 1, 2, 3, 4, 5):")
my_list = [int(x.strip()) for x in user_input.split(",")]
evens = []
odds = []
for n in my_list:
    if n % 2 == 0:
        evens.append(n)
    else:
        odds.append(n)

print(f"Even numbers: {len(evens)}")
print(f"Odd numbers: {len(odds)}")