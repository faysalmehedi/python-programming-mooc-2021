# Write your solution here
limit = int(input("Limit: "))
summ = 1
count = 1
sentence = "The consecutive sum: 1"

while summ < limit:
    count += 1
    summ += count
    sentence += f" + {count}"

print(f"{sentence} = {summ}")