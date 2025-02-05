my_list = ["apple", "banana", "cherry"]
my_list.append("date")
print(f"append('date'): {my_list}")
another_list = ["fig", "grape"]
my_list.extend(another_list)
print(f"extend(['fig', 'grape']): {my_list}")
my_list.insert(1, "apricot") # Insert "apricot" at index 1,
print(f"insert(1, 'apricot'): {my_list}")
my_list.remove("banana")
print(f"remove('banana'): {my_list}")
popped_item = my_list.pop(2) # Remove and return the element at index 2 ("cherry")
print(f"pop(2): {my_list}, popped item:{popped_item}")
index_of_date = my_list.index("date")
print(f"index('date'): {index_of_date}")
my_list.append("apple")  # Add another "apple"
count_of_apple = my_list.count("apple")
print(f"count('apple'): {count_of_apple}")
my_list.reverse()
print(f"reverse(): {my_list}")  # Output:
my_list.sort()
print(f"sort(): {my_list}")
my_list.sort(key=len)
print(f"sort(key=len): {my_list}")
