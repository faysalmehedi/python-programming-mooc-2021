# Write your solution here

w1 = input("Please type in the 1st word: ")
w2 = input("Please type in the 2nd word: ")

if w1 == w2:
    print("You gave the same word twice.")
elif w1 > w2:
    print(f"{w1} comes alphabetically last.")
elif w1 < w2:
    print(f"{w2} comes alphabetically last.")