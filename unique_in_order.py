def unique_in_order(sequence):
    unique_list = []
    for i in range(len(sequence)):
        if i == 0 or sequence[i] != sequence[i-1]:
            unique_list.append(sequence[i])
    return unique_list
