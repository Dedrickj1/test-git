def max_num_in_list(a_list):
    if not a_list:
        return None
    max_num = a_list[0]
    for num in a_list:
        if num > max_num:
            max_num = num
    return max_num
numbers = [10, 3, 9, 35, 20]
result = max_num_in_list(numbers)
print(result)