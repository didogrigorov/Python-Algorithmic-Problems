def fourNumberSum(array, targetSum):
    # Write your code here.
    pair_sums = {}
    quadruplets = []

    for i in range(1, len(array) - 1):
        for j in range(i + 1, len(array)):
            current_sum = array[i] + array[j]
            difference = targetSum - current_sum

            if difference in pair_sums:
                for pair in pair_sums[difference]:
                    quadr = pair + [array[i], array[j]]
                    if quadr in quadruplets:
                        break
                    else:
                        quadruplets.append(pair + [array[i], array[j]])

        for k in range(0, i):
            current_sum = array[i] + array[k]
            if current_sum not in pair_sums:
                pair_sums[current_sum] = [[array[k], array[i]]]
            else:
                pair_sums[current_sum].append([array[k], array[i]])

    return quadruplets



array = [-3,-2,-1,0,0,1,2,3]
targetSum = 0

print(fourNumberSum(array, targetSum))