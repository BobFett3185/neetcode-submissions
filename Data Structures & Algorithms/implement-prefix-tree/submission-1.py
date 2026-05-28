
class node:
    def __init__(self): 
        self.children = {} # this stores all the children of this character (possible next letters)
        self.isEnd = False # this needs to be false because we dont assume everything is the end of a word, 
        # we explicitly mark ends as true

class PrefixTree:

    def __init__(self):
        self.root = node()
        # we instantiate a root node and store an empty space

    def insert(self, word: str) -> None:

        curr = self.root # get the current node 

        for char in word:
            if char not in curr.children: # if the next letter isn't there 
                curr.children[char] = node() # we add it to the current children
            curr = curr.children[char] # then we move to that next letter
        
        curr.isEnd = True # mark the last one as the end 


    def search(self, word: str) -> bool:
        #same kind of traversal logic 
        curr = self.root
        for char in word:
            if char not in curr.children: # if not there 
                return False  # return false 
            curr = curr.children[char] # move forward

        return curr.isEnd # if current is the end then the word is there 
        # if curr.isEnd is false, then the word is not there it just happens to be a prefix of another 


    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children: # if not there then return false 
                return False 
            curr = curr.children[char]
        
        return True # always return true if we make it here 




        
        