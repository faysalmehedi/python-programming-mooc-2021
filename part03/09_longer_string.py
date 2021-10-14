# Write your solution here

input01 = input("Please type in string 1: ")
input02 = input("Please type in string 2: ")

if len(input01) > len(input02):
    print(f"{input01} is longer")
elif len(input01) < len(input02):
    print(f"{input02} is longer")
else:
    print("The strings are equally long")