# Write your solution here

year = int(input("Year: "))
next_year = year + 1

while True:
    if next_year % 4 == 0:
        if next_year % 100 == 0:
            if next_year % 400 == 0:
                print(f"The next leap year after {year} is {next_year}")
                break
        else:
            print(f"The next leap year after {year} is {next_year}")
            break

    next_year += 1
