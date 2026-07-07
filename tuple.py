my_tuple = (1, 2, 3, 2, 4, 5, 2)
print(f"Initial Tuple: {my_tuple}")

# 1. count(): Returns the number of times a specified value occurs
count_2_tuple = my_tuple.count(2)
print(f"1. Count of 2: {count_2_tuple}")

# 2. index(): Searches the tuple for a specified value and returns its position
index_3_tuple = my_tuple.index(3)
print(f"2. Index of 3: {index_3_tuple}")
