my_list = [10, 20, 30, 20, 40, 50]
print(f"Initial List: {my_list}")

# 1. append(): Adds an item to the end of the list
my_list.append(60)
print(f"1. After append(60): {my_list}")

# 2. insert(): Adds an item at a specified index
my_list.insert(1, 15)
print(f"2. After insert(1, 15): {my_list}")

# 3. remove(): Removes the first occurrence of a specified value
my_list.remove(20)
print(f"3. After remove(20): {my_list}")

# 4. count(): Returns the number of times a specified value occurs in a list
count_20 = my_list.count(20)
print(f"4. Count of 20: {count_20}")

# 5. sort(): Sorts the list in ascending order (in-place)
my_list.sort()
print(f"5. After sort(): {my_list}")

# And one more for good measure: reverse()
my_list.reverse()
print(f"   After reverse(): {my_list}")
