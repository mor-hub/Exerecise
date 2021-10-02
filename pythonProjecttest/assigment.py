# user_input = " "
# user_input = input("Hey user, please enter two words divided with a comma!\n")
# print(user_input[0], user_input[1])


# user_input = " "
# user_input = input("Hey user, please enter string!\n")
# first_string = user_input
#
# user_input2 = " "
# user_input2 = input("Hey user, please enter another string and I will add it to the first string!\n")
# second_string = user_input2
# print(first_string, second_string)


# num_list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 110]
# # print(len(num_list))
#
# for i in range(len(num_list)):
#     print(num_list[i])


# row_number = ["x", "xx", "xxx", "xxxx", "xxxxx"]
#
# for i in range(len(row_number)):
#         print(row_number[i])

# sign = "x"
#
# for i in range(len(sign)):
#         print(sign[i])


# sign = "x"
# for i in range(6):
#         for z in range(i):
#                 print(sign, end=" ")
#         print()

# for i in range(1,6):
#         for j in range(i):
#             print("#",end=' ')
#         print()

# sign = "x"
# for i in range(6):
#         for z in range(i):
#                 print("x", end="")
#         print()

piramid_size = str(input("Hey user, please enter a number!\n"))

for row_num in range(int(piramid_size)):
        for spaces in range(int(piramid_size) - row_num):
                print(" ", end="")
        for piramid_row_size in range(row_num + (row_num -1)):
                print("x", end="")
        print()


# user_input = str(input("Hey user, please enter a number!\n"))
# user_input = user_input.split()
# numbers = [int(i) for i in user_input]
# for i in range(len(user_input)):
#         for z in numbers:
#                 print(z + z)

# n = str(input("Hey user, please enter a number!\n"))
# numbers = [int(i) for i in n]
# for n in numbers:
#         print(sum(numbers))
# print(int(n[0]) + int(n[1]))
# n_sum = 0
# for:
        
# number1 = numbers[0]
# number2 = numbers[1]
# (number1 + number2)

# n = str(input("Hey user, please enter a number!\n"))
# def getSum(n):
#         sum = 0
#         for digit in str(n):
#                 sum += int(digit)
#         return sum
#
# z = n
# print(getSum(n))