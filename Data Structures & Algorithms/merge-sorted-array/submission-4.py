class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        write =len(nums1)-1
        # we can write from the end and then reverse

        n1 =m-1 
        n2 =n-1

        while n1>-1 and n2>-1:
            insert = max(nums1[n1], nums2[n2])            
            if insert == nums1[n1]:
                n1-=1 
            else:
                n2-=1 

            nums1[write]= insert
            write-=1

        print(nums1)
        while n2>-1:
            nums1[write]= nums2[n2]
            n2-=1
            write-=1
        





        