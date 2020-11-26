"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur? it will occur when we input an alphabet
2. When will a ZeroDivisionError occur? it will occur when the denominator is 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")