# Write your solution here
while True:
    string = input("Please type in a string: ")
    length = len(string)

    if length == 0:
        print('')
        break
    else:
        print(string)
        print('-' * length)
