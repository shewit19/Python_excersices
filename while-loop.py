# array Searching

def arrayCreation():
    numbers = []
    # Accept the collection from users
    user_input = input|("Enter the numbers separeted by comma: ")
    input_values = user_input.split(",")
    for values in input_values:
        numbers.append(int(values.strip()))
    print(numbers)

    return numbers # it rturns the array that has been created

# Initialize index and boolean flag

def arraySearching(number, arrayName):
    index = 0 
    found = False
    # while loop condition based on the boolean value found
    while index < len(arrayName) and not found:
       if arrayName[index] == number:
           found = True # set found to true if the target is found
       index += 1 # Move to the next index
    
    return found


numbers_array = arrayCreation()
print(numbers_array)

# # set the value we're  looking for
target_value = int(input("Enter the number to search: "))
# # check if the value was found are print the result
if arraySearching(target_value, numbers_array):
    print(f"value {target_value} found in the array.")                
else:
    print(f"value {target_value} not found in the array.")    




 