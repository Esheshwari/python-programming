# Program to merge two dictionaries, handling overlapping keys
def merge_dictionaries():
    print("Enter the first dictionary (key-value pairs separated by spaces):")
    dict1 = input("Example: key1:value1 key2:value2\n").strip()
    
    print("\nEnter the second dictionary (key-value pairs separated by spaces):")
    dict2 = input("Example: keyA:valueA keyB:valueB\n").strip()
    
    # Convert user inputs into dictionaries
    dict1 = {key.strip(): value.strip() for key, value in (item.split(':') for item in dict1.split())}
    dict2 = {key.strip(): value.strip() for key, value in (item.split(':') for item in dict2.split())}
    
    # Merge dictionaries with overlapping keys handled
    merged_dict = dict1.copy()
    for key, value in dict2.items():
        if key in merged_dict:
            # If the key exists, combine values into a list
            if isinstance(merged_dict[key], list):
                merged_dict[key].append(value)
            else:
                merged_dict[key] = [merged_dict[key], value]
        else:
            # If the key doesn't exist, simply add it
            merged_dict[key] = value
    
    print("\nMerged Dictionary:")
    print(merged_dict)

# Run the program
merge_dictionaries()
