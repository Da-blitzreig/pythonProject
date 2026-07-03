def find_maximum(list_of_nums: list):
    index = 0
    highest = list_of_nums[0]
    while index < len(list_of_nums):
        if list_of_nums[index] > highest:
            highest = list_of_nums[index]
        index += 1
    print(highest)
def find_minimum(list_of_nums: list):
    index = 0
    lowest = list_of_nums[0]
    while index < len(list_of_nums):
        if list_of_nums[index] < lowest:
            lowest = list_of_nums[index]
        index += 1
    print(lowest)


one = [56, 76, 36, 87, 4, 62, 36, 99, 85]
find_maximum(one)
find_minimum(one)