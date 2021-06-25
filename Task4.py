my_list = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
my_list2 = [my_list[i] for i in range(len(my_list)) if
            my_list[i] not in my_list[:i] + my_list[-(len(my_list) - i - 1):] or my_list[i] not in my_list[
                                                                                                   :i] and i == len(
                my_list) - 1]
print(my_list2)

