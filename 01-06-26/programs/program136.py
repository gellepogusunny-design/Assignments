def is_triplet(a, b, c):
 # Sort the numbers in ascending order
 sorted_numbers = sorted([a, b, c])
 # Check if the sum of squares of the two smaller numbers equals the
 return sorted_numbers[0] ** 2 + sorted_numbers[1] **2==sorted_numbers
print(is_triplet(3, 4, 5))
