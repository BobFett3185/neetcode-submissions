class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF

        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) & mask
            b = carry & mask

        return a if a <= max_int else ~(a ^ mask)
            

    # we basically keep and a and b to get a sum 
    # x or to get the carry 
    # shift the carry 1 and add the carry to the sum 
    # return once the carry is 0 