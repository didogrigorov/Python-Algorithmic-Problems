from typing import List


def highFive(items: List[List[int]]) -> List[List[int]]:
    students = {}
    result = []
    average = 0

    for i in range(len(items)):
        if items[i][0] not in students:
            students[items[i][0]] = []

        students[items[i][0]].append(items[i][1])

    for key, val in students.items():
        val.sort(reverse=True)
        for i in range(0, 5):
            average += val[i]

        average = average // 5

        result.append([key, average])
        average = 0

    final = sorted(result, key = lambda x: x[0])

    return final


items = [[5,91],[5,92],[3,93],[3,97],[5,60],[3,77],[5,65],[5,87],[5,100],[3,100],[3,76]]

print(highFive(items))
