import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Searching (indices where value matches)
indices = np.where(array1 == search_value)[0]

# Counting occurrences
count = np.count_nonzero(array1 == count_value)

# Broadcasting addition
broadcasted_array = array1 + broadcast_value

# Sorting the array
sorted_array = np.sort(array1)

# Output
print(indices)
print(count)
print(broadcasted_array)
print(sorted_array)
