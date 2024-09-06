# Define the sets
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Perform set operations
union_set = set1.union(set2)  # Union of sets
intersection_set = set1.intersection(set2)  # Intersection of sets
difference_set = set1.difference(set2)  # Difference of sets
is_subset = set1.issubset(set2)  # Checking if set1 is a subset of set2
is_superset = set1.issuperset(set2)  # Checking if set1 is a superset of set2

# Print results
print("Union of sets:", union_set)
print("Intersection of sets:", intersection_set)
print("Difference of sets:", difference_set)
print("subset of sets:", is_subset)
print("superse of sets:", is_superset)
