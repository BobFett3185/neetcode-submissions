
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
            if char not in curr.children:
                return False 
            curr = curr.children[char]

        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return False 
            curr = curr.children[char]
        
        return True



        
        