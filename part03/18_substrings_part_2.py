# Write your solution here

string = input("Please type in a string: ")
length = len(string) -1

while length >= 0 :
    print(string[length:])
    length -= 1


    