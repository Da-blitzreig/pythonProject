def sort_integers(nums):
    result = []
    for num in nums:
        if num % 2 == 0 and num % 3 == 0:
            result.append(num)
    print(result)

numbers = [12, 7, 18, 25, 6, 30, 11, 24]
sort_integers(numbers)