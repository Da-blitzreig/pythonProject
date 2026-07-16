def median_in_list(list_of_num):
    list_of_num.sort()
    n = len(list_of_num)
    middle = n // 2
    if n % 2 == 1:
        print(list_of_num[middle])
    else:
        print((list_of_num[middle - 1] + list_of_num[middle]) / 2)

score = [2, 3, 6, 7, 5]
median_in_list(score)