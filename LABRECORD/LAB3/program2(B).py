# Program to merge two dictionaries

def merge_dictionaries():
    print("Enter the first dictionary (key-value pairs separated by spaces):")
    dict1 = input("Example: key1:value1 key2:value2\n").strip()
    
    print("\nEnter the second dictionary (key-value pairs separated by spaces):")
    dict2 = input("Example: keyA:valueA keyB:valueB\n").strip()
    
    # Convert user inputs into dictionaries
    dict1 = {key.strip(): value.strip() for key, value in (item.split(':') for item in dict1.split())}
    dict2 = {key.strip(): value.strip() for key, value in (item.split(':') for item in dict2.split())}
    
    # Merge the dictionaries
    merged_dict = {**dict1, **dict2}
    
    print("\nMerged Dictionary:")
    print(merged_dict)

# Run the program
merge_dictionaries()
