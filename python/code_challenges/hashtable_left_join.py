from data_structures.hashtable import Hashtable


def left_join(ht_a, ht_b):

    list = []

    if ht_a is not None:
        list.append(ht_a)

    for i in list:
        if list[i] is None:
            list.pop(list[i])

    return list
