# Write your solution here

fahrenheit_temp = int(input("Please type in a temperature (F): "))
celsius_temp = (fahrenheit_temp - 32) * (5/9)

if celsius_temp < 0:
    print(f"{fahrenheit_temp} degrees Fahrenheit equals {celsius_temp} degrees Celsius")
    print("Brr! It's cold in here!")
else:
    print(f"{fahrenheit_temp} degrees Fahrenheit equals {celsius_temp} degrees Celsius")