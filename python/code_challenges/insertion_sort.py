def insertion_sort(list):
    idx_length = range(1, len(list))
    for i in idx_length:
        sort_value = list[i]
        while list[i-1] > sort_value and i>0:
            list[i-1], list[i] = list[i], list[i-1]
            i -= 1
