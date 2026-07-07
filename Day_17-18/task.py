def find_last_in_list(list_of_num: list):
    last = list_of_num[-1]
    print(last)
def find_third_in_list(list_of_num: list):
    last = list_of_num[2]
    print(last)
def median_in_list(list_of_num: list):
    n = len(list_of_num)
    middle = n // 2
    if n % 2 == 1:
        print(list_of_num[middle])
    else:
        print(list_of_num[middle - 1], list_of_num[middle])
one = [11, 72, 15, 14, 19, 1671, 12]
two = [11, 72, 15, 0, 19, 1671, 12]
three = [11, 72, 15, 0, 1, 1671, 12, 97]
four = [11, 72, 15, 13, 2, 3, 1671, 44, 12, 97]
five = [11, 72, 15, 13, 14, 4, 1671, 44, 12, 97, 99]
find_last_in_list(one)
find_third_in_list(one)
median_in_list(three)


## test your  median_in_list with the below lista:
# 1_odd. [11, 72, 15, 0, 19, 1671, 12]
# 2_even. [11, 72, 15, 0, 1, 1671, 12, 97]
# 3_even. [11, 72, 15, 13, 2, 3, 1671, 44, 12, 97]
# 4_odd. [11, 72, 15, 13, 14, 4, 1671, 44, 12, 97, 99]