# Write your solution here

name = input("Please tell me your name: ")

if name == "Jerry":
    print("Next please!")
else:
    portions_of_soup = int(input("How many portions of soup?"))
    print(f"The total cost is {portions_of_soup * 5.90}")
    print("Next please!")