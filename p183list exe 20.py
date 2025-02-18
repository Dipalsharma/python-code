def check_first_last(lst):
    if len(lst) > 0 and lst[0] == lst[-1]:
        return True
    return False
list1 = [100, 200, 320, 40, 100]
list2 = [751, 6, 3, 5, 9]
print("Result for list1:", check_first_last(list1))
print("Result for list2:", check_first_last(list2))
