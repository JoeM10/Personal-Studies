import sys

# Get user input
user_input = input("Enter a string: ")

# Convert each character to its ASCII value and store in a list
ascii_values = [ord(char) for char in user_input]

# Print the list of ASCII values
print("ASCII values:", ascii_values)

# Calculate and print the memory usage of the string
string_memory_usage = sys.getsizeof(user_input)
print("Memory usage of the string:", string_memory_usage, "bytes")

# Print the memory location of the string
string_memory_location = id(user_input)
print("Memory location of the string:", string_memory_location)





# beginning flag - > data - > ending flag