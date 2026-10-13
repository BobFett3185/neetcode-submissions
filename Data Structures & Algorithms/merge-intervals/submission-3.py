class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        result = []
        for i in range(len(intervals)-1):
            first = intervals[i]
            second = intervals[i+1]

            # compare the last of first and first of second, do they overlap???
            if first[1] >= second[0]:
                intervals[i+1] = [first[0], max(first[1], second[1])]
            else:
                result.append(first)
        result.append(intervals[-1])
        return result