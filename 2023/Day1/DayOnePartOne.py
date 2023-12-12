# Function to find the first and last digit in a string and concatenate them
def find_and_concatenate(s):
    # Initialize a variable to store the first digit; starts empty
    first_digit = ""
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a digit
        if char.isdigit():
            # If it's a digit, store it as the first digit
            first_digit = char
            # Break out of the loop; no need to check further
            break

    # Initialize a variable to store the last digit; starts empty
    last_digit = ""
    # Iterate over each character in the string in reverse order
    for char in reversed(s):
        # Check if the character is a digit
        if char.isdigit():
            # If it's a digit, store it as the last digit
            last_digit = char
            # Break out of the loop; no need to check further
            break

    # Check if both a first and a last digit were found
    if first_digit and last_digit:
        # Concatenate the digits and convert the string to an integer
        result = int(first_digit + last_digit)
    else:
        # If either digit is missing, set result to None
        result = None

    # Return the result (either an integer or None)
    return result

# Function to read from a file and sum the numbers obtained from each line
def read_file_and_sum_numbers(file_path):
    # Initialize a variable to hold the total sum; starts at 0
    total_sum = 0

    # Open the file at the given path for reading ('r')
    with open(file_path, 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Process the line to strip any leading/trailing whitespace and find the number
            number = find_and_concatenate(line.strip())
            # Check if a number was successfully found
            if number is not None:
                # Add the number to the total sum
                total_sum += number

    # Return the total sum
    return total_sum


# Replace 'input.txt' with the path to your text file
file_path = 'C:\\Users\\vince\\AOC\\2023\\Day1\\Input\\input.txt'
total = read_file_and_sum_numbers(file_path)
print("The sum of all numbers is:", total)
