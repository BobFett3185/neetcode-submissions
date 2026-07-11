class Solution:
    def reverseBits(self, n: int) -> int:
        res =0
        for i in range(32):
            bit = (n >> i) & 1
            res = res | (bit << (31-i))
        return res
    '''
    We can go through and for every bit of the 32 bits 
    we shift to the right by to isolate the ith bit. Then and it with 1 to get what the bit is 
    Then in res we can update it by doing the or operation of the bit and the spot in res  shifted left 
    by 31 -i (that way we can reverse it )
    '''