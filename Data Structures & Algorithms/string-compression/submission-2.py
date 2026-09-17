
class Solution:
    def compress(self, chars: List[str]) -> int:
        read =0 
        write =0 
        # we keep the write pointer at the front and then read goes forward

        while read<len(chars):
            #when we see a character we always write it 
            chars[write]=chars[read]
            read+=1 
            write+=1
            
            # if there are multiple instances of what we just read:
            if read <len(chars) and chars[read]==chars[read-1]:
                count = 1
                while read<len(chars) and chars[read]==chars[read-1]:
                    count+=1 
                    read+=1

                for digit in str(count):
                    chars[write] = digit
                    write+=1

        return write