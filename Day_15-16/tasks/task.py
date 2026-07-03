def print_list(list_of_nums: list):
    index = 0
    highest = list_of_nums[0]   # Start with the first number
    while index < len(list_of_nums):
        if list_of_nums[index] > highest:
            highest = list_of_nums[index]
        index += 1
    print(highest)


one = [56, 76, 36, 87, 4, 62, 36, 99, 85]
print_list(one)