def merge_sort(list):
    print(f'merge_sort {list}')
    if len(list) > 1:
        left_list = list[:len(list)//2]
        right_list = list[len(list)//2:]
        # recursion
        merge_sort(left_list)
        merge_sort(right_list)
        print(f'left_list {left_list}, right_list {right_list}')
        # merge
        i = 0 # left_list index
        j = 0 # right_list index
        k = 0 # merged list index
        while i < len(left_list) and j < len(right_list):
            print(f'We compare the two values and selecting the smallest value of {left_list[i]} and {right_list[j]}.')
            if left_list[i] < right_list[j]: # compares the left index with the right
                list[k] = left_list[i] # save the value of the left to the merged list
                i += 1
            else:
                list[k] = right_list[j] # save the value of the right to the merged list
                j += 1
            print(f'{list[k]} is the smallest value, so we append it to the merged list.')
            k += 1
            print(list)

        # transferring the remaining value to the merged list
        while i < len(left_list):
            print(f'We will append remaining value {left_list[i]} to the merged list.')
            list[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            print(f'We will append remaining value {right_list[j]} to the merged list.')
            list[k] = right_list[j]
            j += 1
            k += 1
