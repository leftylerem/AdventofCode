def ParseString(str):
    left = "0"
    right = "0"
    for char in str:
        if char.isnumeric():
            left = char
            break 
    for char in reversed(str):
        if char.isnumeric():
            right = char
            break
    return int(left + right) 
# Open the file in read mode ('r')
with open('input.txt', 'r') as file:
    # Read the entire file content into a string
    content = file.readlines()  
    sum = 0
    for line in content:
        sum += ParseString(line)
    print(sum)
#turn string into array
#find out if its a digit 
#if it is, stop
#save digit
#reverse array 
#find out if its a digit
#if it is, stop
#save digit
#return digits
