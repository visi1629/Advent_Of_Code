def find_and_concatenate(s):
  

    # Define the mapping for words to numbers
    word_to_num = {
        'one': 1, 'two': 2, 'three': 3, 'four': 4, 
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    def find_numbers(s):
        """
        Objective of this function is to find the first and last digits, one the first digit is identified it is stored,
        the last digit is found by going through the string incrimentaly and continuly overwriting the last found string untill
        the string is completely scanned.
        """
        first_num = None 
        last_num = None   

        # Loop through each character in the string
        for i in range(len(s)):
            # Check if the current character is a digit
            if s[i].isdigit():
                num = int(s[i])  # Convert digit to an integer
            # Check if the current substring of length 3 is a number word
            elif i >= 2 and s[i-2:i+1] in word_to_num:
                num = word_to_num[s[i-2:i+1]]
            # Check if the current substring of length 4 is a number word
            elif i >= 3 and s[i-3:i+1] in word_to_num:
                num = word_to_num[s[i-3:i+1]]
            # Check if the current substring of length 5 is a number word
            elif i >= 4 and s[i-4:i+1] in word_to_num:
                num = word_to_num[s[i-4:i+1]]
            else:
                continue  # Continue to next iteration if no condition is met

            # If first_num is still None, assign the current number to it
            if first_num is None:
                first_num = num
            # Update last_num with the current number
            last_num = num

        return first_num, last_num  # Return the first and last numbers found

    # Use the find_numbers function to get the first and last numbers
    first_digit, last_digit = find_numbers(s)
    
    # If both first and last numbers are found, concatenate them into a new number
    if first_digit is not None and last_digit is not None:
        return int(f"{first_digit}{last_digit}")
    # If either the first or last number is not found, return None
    return None

        

   
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
file_path = 'C:\\Users\\vince\\AOC\\2023\\Day1\\strings.txt'
total = read_file_and_sum_numbers(file_path)
print("The sum of all numbers is:", total)
