class Solution:

    def shipWithinDays(self, weights, D):
        if not weights:
            return 1

        lo = max(weights)
        hi = sum(weights)

        while lo < hi:
            capacity = lo + (hi - lo) // 2

            # Test this capacity
            current_load = 0
            days = 1

            for i in range(len(weights)):
                if weights[i] + current_load > capacity:
                    current_load = weights[i]
                    days += 1
                else:
                    current_load += weights[i]

            if days <= D:
                hi = capacity
            else:
                lo = capacity + 1

        return lo