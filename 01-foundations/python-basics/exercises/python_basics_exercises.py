"""
Python Basics Exercises for Data Science
Run this file directly.
"""

print("\n========== EXERCISE 1: Variables & Data Types ==========")
# Q: Store age, height, name, learning_ds and print in one sentence

# Solution
age = 25
height = 5.8
name = "Chitta"
learning_ds = True
print(f"My name is {name}, age {age}, height {height}, learning DS: {learning_ds}")


print("\n========== EXERCISE 2: Lists & Aggregations ==========")
# Q: Find sum, average, max of numbers

numbers = [10, 20, 30, 40, 50]

# Solution
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)

print("Sum:", total)
print("Average:", average)
print("Max:", maximum)


print("\n========== EXERCISE 3: Dictionary Filtering ==========")
# Q: Print students scoring more than 75

students = {"Amit": 82, "Rahul": 68, "Sneha": 91, "Priya": 74}

# Solution
for name, marks in students.items():
    if marks > 75:
        print(name, marks)


print("\n========== EXERCISE 4: Functions ==========")
# Q: Return mean, min, max from a list

# Solution
def calculate_stats(data):
    return {
        "mean": sum(data) / len(data),
        "min": min(data),
        "max": max(data)
    }

print(calculate_stats([5, 10, 15, 20]))


print("\n========== EXERCISE 5: File Handling ==========")
# Q: Write numbers to file and compute average

# Solution
with open("numbers.txt", "w") as f:
    f.write("10\n20\n30\n40")

nums = []
with open("numbers.txt") as f:
    for line in f:
        nums.append(int(line.strip()))

print("Average:", sum(nums) / len(nums))


print("\n========== EXERCISE 6: Error Handling ==========")
# Q: Safe division

# Solution
try:
    a, b = 10, 0
    print("Result:", a / b)
except ZeroDivisionError:
    print("Cannot divide by zero")


print("\n========== EXERCISE 7: List Comprehension ==========")
# Q: Square only even numbers

nums = [1, 2, 3, 4, 5, 6]

# Solution
squares = [x**2 for x in nums if x % 2 == 0]
print(squares)


print("\n========== EXERCISE 8: Data Cleaning ==========")
# Q: Remove None and convert to int

raw_data = ["10", None, "20", "30", None]

# Solution
cleaned = [int(x) for x in raw_data if x is not None]
print(cleaned)


print("\n========== EXERCISE 9: OOP ==========")
# Q: Dataset class with mean method

# Solution
class Dataset:
    def __init__(self, data):
        self.data = data

    def mean(self):
        return sum(self.data) / len(self.data)

ds = Dataset([10, 20, 30])
print(ds.mean())


print("\n========== EXERCISE 10: Mini Data Science Task ==========")
# Q: Total sales per day

sales = [
    {"day": "Mon", "amount": 100},
    {"day": "Tue", "amount": 150},
    {"day": "Mon", "amount": 200}
]

# Solution
summary = {}
for s in sales:
    summary[s["day"]] = summary.get(s["day"], 0) + s["amount"]

print(summary)
