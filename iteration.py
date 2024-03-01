import random

my_list = []

for i in range(50):
    x = random.randint(1, 10)
    my_list.append(x)

print(my_list)

# Count occurrences of each number
num_counts = {}
for num in my_list:
    if num in num_counts:
        num_counts[num] += 1
    else:
        num_counts[num] = 1

# Find the maximum count
max_count = max(num_counts.values())

# Find the number(s) with the maximum count
max_iterated_num = [num for num, count in num_counts.items() if count == max_count]

print(f"{max_iterated_num} appeared {max_count} times.")

