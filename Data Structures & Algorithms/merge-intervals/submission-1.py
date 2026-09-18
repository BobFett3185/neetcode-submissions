class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals = sorted(intervals)
        intervals.append([100000,0])
        print(intervals)
        output = []
        for i in range(len(intervals)-1):
            # only add to output when valid 
            if intervals[i][1] >= intervals[i+1][0]: # merge 
                intervals[i+1]=[intervals[i][0], max(intervals[i+1][1], intervals[i][1])]
            else:
                output.append(intervals[i])

        return output

