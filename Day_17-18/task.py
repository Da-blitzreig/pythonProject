def find_last_in_list(list_of_num: list):
    last = list_of_num[-1]
    print(last)
def find_third_in_list(list_of_num: list):
    last = list_of_num[2]
    print(last)
def median_in_list(list_of_num:list):
    median_of_list = len(list_of_num)
    median1 = int(median_of_list / 2)
    medians = median1 - 1
    median = list_of_num[median1]
    print(median)

one = [11, 72, 15, 14, 19, 1671, 12]

find_last_in_list(one)
find_third_in_list(one)
median_in_list(one)

## test your  median_in_list with the below lista:
# 1_odd. [11, 72, 15, 0, 19, 1671, 12]
# 2_even. [11, 72, 15, 0, 1, 1671, 12, 97]
# 3_even. [11, 72, 15, 13, 2, 3, 1671, 44, 12, 97]
# 4_odd. [11, 72, 15, 13, 14, 4, 1671, 44, 12, 97, 99]