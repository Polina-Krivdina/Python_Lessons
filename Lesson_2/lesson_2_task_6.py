def filter_list(lst):
    result = [num for num in lst if num < 30 and num % 3 == 0]
    return result
    
lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]

list_filter = filter_list(lst)
print(list_filter)