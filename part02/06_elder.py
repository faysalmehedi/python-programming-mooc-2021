# Write your solution here

print("Person 1: ")
n1 = input("Name: ")
a1 = int(input("Age: "))
print("Person 2: ")
n2 = input("Name: ")
a2 = int(input("Age: "))

if a1 > a2:
    print(f"The elder is {n1}")
elif a1 < a2:
    print(f"The elder is {n2}")
else:
    print(f"{n1} and {n2} are the same age")