n = int(input("Enter the length of the sequence: ")) # Do not change this line

# Formula; Find the sum of the first 3 numbers for n times

num_1, num_2, num_3 = 0, 1, 2

for i in range (n):
    if i == 0:
        print (1,)

    elif i == 1:
        print (2,)

    else:
        sum_num = num_1 + num_2 + num_3
        print(sum_num)
        num_1 = num_2
        num_2 = num_3
        num_3 = sum_num
