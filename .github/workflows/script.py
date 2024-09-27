import sys

if len(sys.argv) != 2:
    print("Usage: python process_list.py 'value1,value2,value3,...'")
    sys.exit(1)

input_string = sys.argv[1]
items = input_string.split(',')

# Get unique first values
unique_items = sorted(set(items))
if unique_items:
    unique_items=unique_items[0]

# Output the result as a newline-separated string
print("\n".join(unique_items))
