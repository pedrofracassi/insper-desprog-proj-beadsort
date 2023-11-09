def beadsort(input_list):
    print(input_list)
    """Bead sort."""
    return_list = []
    # Initialize a 'transposed list' to contain as many elements as
    # the maximum value of the input -- in effect, taking the 'tallest'
    # column of input beads and laying it out flat
    transposed_list = [0] * max(input_list)

    for num in input_list:
        print(transposed_list)
        # For each element (each 'column of beads') of the input list,
        # 'lay the beads flat' by incrementing as many elements of the
        # transposed list as the column is tall.
        # These will accumulate atop previous additions.
        transposed_list[:num] = [n + 1 for n in transposed_list[:num]]

    print(transposed_list)

    # We've now dropped the beads. To de-transpose, we count the
    # 'bottommost row' of dropped beads, then mimic removing this
    # row by subtracting 1 from each 'column' of the transposed list.
    # When a column does not reach high enough for the current row,
    # its value in transposed_list will be <= 0.
    for i in range(len(input_list)):
        # Counting values > i is how we tell how many beads are in the
        # current 'bottommost row'. Note that Python's bools can be
        # evaluated as integers; True == 1 and False == 0.
        return_list.append(sum(n > i for n in transposed_list))
    # The resulting list is sorted in descending order

    print(return_list)

    return return_list

beadsort([5, 3, 1, 7, 4, 1, 1, 20])