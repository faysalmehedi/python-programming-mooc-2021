# Write your solution here

string = input("Please type in a string: ")
str_len = len(string)

while str_len > 0:
    print(string[str_len-1])
    str_len -= 1