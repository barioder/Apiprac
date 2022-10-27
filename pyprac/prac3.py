def find_max(nums):
    max_num = float("-inf") #smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num

list = [0.1,800, 5, 0.01, 100]

print(find_max(list))