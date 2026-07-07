set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# 1. add(): Adds an element to the set
set_a.add(5)
print(f"1. After set_a.add(5): {set_a}")

# 2. remove(): Removes a specified element. Raises KeyError if element not found.
#    discard() also removes but does not raise an error if the element is not present.
set_a.remove(1)
print(f"2. After set_a.remove(1): {set_a}")

# 3. union(): Returns a new set containing all elements from both sets
union_set = set_a.union(set_b)
print(f"3. Union of A and B: {union_set}")

# 4. intersection(): Returns a new set containing only the elements common to both sets
intersection_set = set_a.intersection(set_b)
print(f"4. Intersection of A and B: {intersection_set}")

# 5. difference(): Returns a new set with elements in the first set but not in the second
difference_set = set_a.difference(set_b)
print(f"5. Difference (A - B): {difference_set}")
