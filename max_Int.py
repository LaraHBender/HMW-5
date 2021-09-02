num_int = int(input("Input a number: "))    # Do not change this line

# Fill in the missing code

max_int = 0

while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int >= max_int:
        max_int = num_int
    
    else:
        max_int = max_int
    
else:
    max_int = max_int

print()
print("The maximum is", max_int)    # Do not change this line