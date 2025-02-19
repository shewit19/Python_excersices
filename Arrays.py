# # array declaration
# hotels=[] # this is an empty array

# for i in range(0,5):
#     hotel_input= input('Enter the hotel name:' )
#     hotels.append(hotel_input)

# print(hotels)
  

user_input= input('Enter  values  separated by commas: ')

# splitting the input into a list
input_values=  user_input.split(',')

# initialize an empty list 
result_array= []

# loop throgh the input values and append to the array 
for value in input_values:
    # strip any extra whitespace and append to the result array 
    result_array.append(value.strip())

# output the result array 
print("Resulting Array:", result_array)