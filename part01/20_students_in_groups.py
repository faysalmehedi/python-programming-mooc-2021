# Write your solution here
students = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))

groups = students // group_size
lasting = students % group_size

if lasting:
    print(f"Number of groups formed: {groups + 1}")
else:
    print(f"Number of groups formed: {groups}")