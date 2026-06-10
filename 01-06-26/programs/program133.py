def unique(numbers):
 # Use a dictionary to count occurrences of each number
 count_dict = {}

 # Count occurrences of each number in the list
 for num in numbers:
   if num in count_dict:
      count_dict[num] += 1
   else:
      count_dict[num] = 1
 for num, count in count_dict.items():
    if count == 1:
     return num
print(unique([3, 3, 3, 7, 3, 3]))
