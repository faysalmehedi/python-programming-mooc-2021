# Write your solution here

password = input("Password: ")

while True:
    repeat_pass = input("Repeat password: ")
    if password == repeat_pass:
        print("User account created!")
        break
    print("They do not match!")