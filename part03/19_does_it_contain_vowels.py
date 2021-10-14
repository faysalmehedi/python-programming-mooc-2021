# Write your solution here

string = input("Please type in a string: ")
vowels = 'aeo'
i = 0

while i < len(vowels):
    if vowels[i] in string:
        print(f"{vowels[i]} found") 
    else:
        print(f"{vowels[i]} not found") 
    
    i += 1