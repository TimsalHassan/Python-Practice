'''
Our football team has finished the championship. Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format x:y, where x is our team and y is our opponents score. The rules to calculate score is 

If x > y: 3 points

If x < y: 0 point

If x = y: 1 point

We need to write a function that takes this collection and returns the number of points our team (x) got in the championship by the rules given above.'''

# def calculate_points(matches):
#     total_points = 0
    
#     for match in matches:
#         x, y = map(int, match.split(':'))  # Split the match string and convert x, y to integers
        
#         if x > y:
#             total_points += 3
#         elif x == y:
#             total_points += 1
    
#     return total_points

# # Example usage:
# matches = ["2:1", "1:3", "4:4", "3:0", "2:2"]
# points = calculate_points(matches)
# print("Total points:", points)



# import re

# def decode_grid(grid):
#     # Transpose the grid
#     transposed_grid = list(zip(*grid))
    
#     # Join each row into a string and remove non-alphanumeric characters
#     decoded_strings = [''.join(re.findall(r'\w', row)) for row in transposed_grid]
    
#     # Concatenate the resulting strings
#     decoded_string = ''.join(decoded_strings)
    
#     return decoded_string

# # Input grid
# grid = [
#     "Tsi",
#     "h%x",
#     "i #",
#     "sM $a",
#     "#t%",
#     "ir!",
# ]

# print(decode_grid(grid))  # Output: "ThisisMatrix#!"






# # def print_digits_separate_lines(number):
# #     # Handle negative numbers by converting them to positive
# #     if number < 0:
# #         number = abs(number)
    
# #     # Get the number of digits in the integer
# #     num_digits = len(str(number))
    
# #     # Extract each digit and print it in a separate line
# #     for _ in range(num_digits):
# #         # Extract the last digit using modulo operation
# #         digit = number % 10
        
# #         # Print the digit
# #         print(digit)
        
# #         # Remove the last digit from the number
# #         number //= 10

# # # Example usage:
# # input_number = int(input("Enter the numbers: "))
# # print("Digits in separate lines:")
# # print_digits_separate_lines(input_number)


# # def print_digits_separate_lines(number):
# #     # Handle negative numbers by converting them to positive
# #     if number < 0:
# #         number = abs(number)
    
#     # Extract each digit and print it in a separate line
#     while number > 0:
#         # Extract the last digit using modulo operation
#         digit = number % 10
        
#         # Print the digit
#         print(digit)
        
#         # Remove the last digit from the number
#         number //= 10

# # Example usage:
# input_number = int(input("Enter the number: "))
# print("Digits in separate lines:")
# print_digits_separate_lines(input_number)





from functools import reduce
list = [1,2,3,4,5]
def sum (x,y):
    return x+y
print(reduce(sum, list))
