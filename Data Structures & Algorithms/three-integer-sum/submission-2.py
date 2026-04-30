class Solution:
    # basically go through and find 2 numbers
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        # takes index and value of nums as i and a 
        for i, a in enumerate(nums):
            if i > 0 and a==nums[i-1]: #if a duplicate of last element 
                continue
            
            # create 2 ptrs
            l = i+1
            r= len(nums)-1
            while l< r:
                threeSum = a+ nums[l] + nums[r]
                if threeSum > 0:
                    r-=1
                elif threeSum < 0:
                    l+=1 
                else:
                    res.append([a, nums[l], nums[r]])
                    l+=1
                    while nums[l] == nums[l-1] and l< r:
                        l+=1
        return res




        








'''nums.sort()
        blanks = []

        # creates a list of indexes
        for i in range(len(nums)):
            blanks.append(i)  
    
        # set containing all the elements as keys and index as pair value
        elements = dict(zip(nums,blanks))

        answers = set()

        for i in range (len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j]*-1 in elements: 
                    k = elements[nums[i] + nums[j]*-1]
                    if i != k and k!=j and j!=i:
                        answer = tuple(sorted([nums[i], nums[j],(nums[i] + nums[j]*-1)]))
                        answers.add(answer)

        return [list(answer) for answer in answers]
        '''

