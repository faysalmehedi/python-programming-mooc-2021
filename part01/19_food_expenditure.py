# Write your solution here

eat_times = int(input("How many times a week do you eat at the student cafeteria?"))
lunch_price = float(input("The price of a typical student lunch?"))
groceries = float(input("How much money do you spend on groceries in a week?"))

weekly = (eat_times * lunch_price) + groceries
daily = weekly / 7

print(f"""
Average food expenditure:
Daily: {daily} euros
Weekly: {weekly} euros
""")