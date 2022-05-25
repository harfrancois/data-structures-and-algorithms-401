# Merge Sort
First we split the list in two. We'll start with the first half and break it down in to smaller individual list.

merge_sort [8, 4, 23, 42, 16, 15]
merge_sort [8, 4, 23]
merge_sort [8]
merge_sort [4, 23]
merge_sort [4]
merge_sort [23]
left_list [4], right_list [23]

We compare the two values and selecting the smallest value of 4 and 23.
4 is the smallest value, so we append it to the merged list.

[4, 23]

We will append remaining value 23 to the merged list.
left_list [8], right_list [4, 23]
We compare the two values and selecting the smallest value of 8 and 4.
4 is the smallest value, so we append it to the merged list.

[4, 4, 23]

We compare the two values and selecting the smallest value of 8 and 23.
8 is the smallest value, so we append it to the merged list.

[4, 8, 23]

We will append remaining value 23 to the merged list. Next we'll do the same with the other half.

merge_sort [42, 16, 15]
merge_sort [42]
merge_sort [16, 15]
merge_sort [16]
merge_sort [15]
left_list [16], right_list [15]

We compare the two values and selecting the smallest value of 16 and 15.
15 is the smallest value, so we append it to the merged list.

[15, 15]

We will append remaining value 16 to the merged list.

left_list [42], right_list [15, 16]

We compare the two values and selecting the smallest value of 42 and 15.
15 is the smallest value, so we append it to the merged list.

[15, 16, 15]

We compare the two values and selecting the smallest value of 42 and 16.
16 is the smallest value, so we append it to the merged list.

[15, 16, 15]

We will append remaining value 42 to the merged list.

left_list [4, 8, 23], right_list [15, 16, 42]

We compare the two values and selecting the smallest value of 4 and 15.
4 is the smallest value, so we append it to the merged list.

[4, 4, 23, 42, 16, 15]

We compare the two values and selecting the smallest value of 8 and 15.
8 is the smallest value, so we append it to the merged list.

[4, 8, 23, 42, 16, 15]

We compare the two values and selecting the smallest value of 23 and 15.
15 is the smallest value, so we append it to the merged list.

[4, 8, 15, 42, 16, 15]

We compare the two values and selecting the smallest value of 23 and 16.
16 is the smallest value, so we append it to the merged list.

[4, 8, 15, 16, 16, 15]

We compare the two values and selecting the smallest value of 23 and 42.
23 is the smallest value, so we append it to the merged list.

[4, 8, 15, 16, 23, 15]

We will append remaining value 42 to the merged list.
Finally, we end up with a sorted list.

[4, 8, 15, 16, 23, 42]
