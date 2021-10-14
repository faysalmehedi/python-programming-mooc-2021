# Write your solution here

string = input("Please type in a string: ")
i = 0

while i < len(string):
    print(string[0:i+1])
    i += 1