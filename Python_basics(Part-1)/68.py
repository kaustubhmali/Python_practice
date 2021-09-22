number = int(input("Enter the number: "))

sum_of_digits = 0

for digits in str(number):
    print(digits)
    sum_of_digits += int(digits)

print(f"Sum of digits: {sum_of_digits}")