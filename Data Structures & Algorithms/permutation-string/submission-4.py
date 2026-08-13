class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1map = defaultdict(int)
        for char in s1:
            s1map[char]+=1

        tempMap = defaultdict(int)

        left =0
        for right in range(len(s2)):
            if right - left +1 >len(s1):
                tempMap[s2[left]]-=1
                if tempMap[s2[left]]==0:
                    del tempMap[s2[left]]
                left+=1
            tempMap[s2[right]]+=1
            
            if tempMap == s1map:
                return True 
        return False

            

            


            