def isValidSubsequence(array, sequence):
    sequence_idx = 0
    for val in range(len(array)):
        if sequence_idx >= len(sequence):
            break
        if array[val] == sequence[sequence_idx]:
            sequence_idx += 1
    return sequence_idx == len(sequence)
