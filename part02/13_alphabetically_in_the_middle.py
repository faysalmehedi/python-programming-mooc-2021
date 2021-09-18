# Write your solution here

l1 = input("1st letter: ")
l2 = input("2nd letter: ")
l3 = input("3rd letter: ")

if ((l1 > l2) and (l1 < l3)) or ((l1 < l2) and (l1 > l3)):
    print(f"The letter in the middle is {l1}")
elif ((l2 > l1) and (l2 < l3)) or ((l2 < l1) and (l2 > l3)):
    print(f"The letter in the middle is {l2}")
else:
    print(f"The letter in the middle is {l3}")
    