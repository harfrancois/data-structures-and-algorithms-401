# Insertion Sort Blog

let's sort this array with insertion sort.
array = [8,4,23,42]

First thing we need to do is find the starting index which is index 1, and that is 4. So now we set some variable. We'll
set the starting index at index one, and we'll call it temp. Next we need to set J to temp -1. J is set to the index to
the left of what ever index temp is. J will be the number used to compare temp with.

    index  0  1  2   3   4
          [8, 4, 23, 42, 16]

    temp = idx[1], ---> number 4 in the array
    J = temp[i] - 1, ---> number 8 in the array

Using a for loop we'll iterate through the array index until the end of the array. With in the for loop, we'll use a
while loop to compare the number at J with the number at temp. If the number at J is greater than the number at Temp,
we'll swap those number. If it's not we'll move on to the next index.

    FOR i = 1 to arr.length
        WHILE j >= 0 AND temp < arr[j]


We'll start off comparing 4 and 8. Is 4 greater than 8? it's not, so we swap 4 with 8 and move on to the next index.

    [8 > 4, 23, 42, 16] = [4, 8, 23, 42, 16]

Temp become index 2 which is 23 and J is now 8. We'll compare 23 to 8. Is 23 greater than 8? It is so we do not swap the
number and just move on to the next index.

    [4, 8 > 23, 42, 16] = [4, 8, 23, 42, 16]

Temp becomes index 3 which is 42 and J is now 23. We'll compare 42 to 23. Is 42 greater than 23? It is so we do not swap
the numbers and just move on to the next index.

    [4, 8, 23 > 42, 16] = [4, 8, 23, 42, 16]

Temp becomes index 4 which is 16 and J is now 42. we'll compare 16 to 42. Is 16 greater than 42? It's not so we swap
those 2 numbers. Now moving down the left. We'll compare 16 to 23. Is 16 greater than 23. It not so we swap those 2
number. We'll compare 16 to 8. Is 16 greater than 8? It is, so since we are now at the end of the array length. The
list is now sorted.

    [4, 8, 23, 42 > 16] = [4, 8, 23, 16, 42]

    [4, 8, 23 > 16, 42] = [4, 8, 16, 23, 42]

    [4, 8 > 16, 23, 42] = sorted array [4, 8, 16, 23, 42]

