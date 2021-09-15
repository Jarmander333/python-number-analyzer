print("Integer Test!") # Prints the name of the program

test_num = float(input("Please input a number: ")) # Asks the user for the number

if (test_num % 2) == 0: # Checks if the number is even
    print("Test 1: Even")
else: # If it's not even, it's odd
    print("Test 1: Odd")

if test_num < 0: # Checks if the number is negative
    print("Test 2: Negative")
else: # If it's not negative, it's positive
    print("Test 2: Positive")

if -100 > test_num > 100: # Checks if the number is within -100 to 100
    print("Test 3: Exclusive")
else: If it's not, it's outside the range
    print("Test 3: Inclusive")
