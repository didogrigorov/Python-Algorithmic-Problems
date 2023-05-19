from typing import List


def generate(numRows: int) -> List[List[int]]:
    result = [[1]]

    for i in range(numRows - 1):
        temp = [0] + result[-1] + [0]
        row = []

        for j in range(len(result[-1]) + 1):
            row.append(temp[j] + temp[j + 1])

        result.append(row)

    return result

# def generate(rowIndex) -> List[List[int]]:
#     if rowIndex == 0:
#         return [[1]]
#     else:
#         return getAllRow(rowIndex - 1)
#
# def getAllRow(rowIndex):
#     if rowIndex == 0:
#         return [[1]]
#
#     ListPrec = getAllRow(rowIndex - 1)
#
#     Len = len(ListPrec[-1])
#
#     ListPrec.append([1])
#
#     for i in range(0, Len - 1):
#         ListPrec[-1].append(ListPrec[-2][i] + ListPrec[-2][i + 1])
#
#     ListPrec[-1].append(1)
#
#     return ListPrec


print(generate(5))