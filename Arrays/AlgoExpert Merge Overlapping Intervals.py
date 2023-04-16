def merge(intervals: List[List[int]]) -> List[List[int]]:
    sortedIntervals = sorted(intervals, key=lambda x: x[0])

    merged = []
    currentInterval = sortedIntervals[0]
    merged.append(currentInterval)

    for nextInterval in sortedIntervals:
        _, current_end = currentInterval
        nextIntervalStart, nextIntervalEnd = nextInterval

        if current_end >= nextIntervalStart:
            currentInterval[1] = max(current_end, nextIntervalEnd)
        else:
            currentInterval = nextInterval
            merged.append(currentInterval)

    return merged



intervals = [
    [1, 10],
    [10, 20],
    [20, 30],
    [30, 40],
    [40, 50],
    [50, 60],
    [60, 70],
    [70, 80],
    [80, 90],
    [90, 100]
]

print(mergeOverlappingIntervals(intervals))