class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hash map with values as keys and pair is frequency
        # freq is a list of lists 
        # for each element in the dict, add the num in the list with index of the frequency 
        # return the last k numbers 
        
        count = {} #keys are the elements of nums
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums: # add frequencies to count
            count[num] = 1 + count.get(num, 0)
        for num, cnt in count.items(): # takes those pairs and stores in frequency lists
            freq[cnt].append(num)
            # the cnt index is the frequency from the count map 
            # the num is the value from nums that you append to the correct frequency list

        res = [] # create a result list 
        for i in range(len(freq) - 1, 0, -1): # go backwards 
            for num in freq[i]: #start adding numbers to list 
                res.append(num)
                if len(res) == k: # return result when it has k numbers
                    return res

            