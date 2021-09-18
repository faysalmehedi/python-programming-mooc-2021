# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
numbers_sum = 0
positive = 0
negative = 0

while True:
    number = int(input("Number: "))

    if number == 0:
        break

    if number >= 0:
        positive += 1
    else:
        negative += 1

    count += 1
    numbers_sum += number

print(f"Numbers typed in {count}")
print(f"The sum of the numbers is {numbers_sum}")
print(f"The mean of the numbers is {numbers_sum / count}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")