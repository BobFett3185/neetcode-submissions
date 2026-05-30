class letter:
    def __init__(self):
        self.children = {}
        self.end = False
    
class WordDictionary:
    def __init__(self): # make our tree here
        self.root = letter()
        
    # pretty simple same as last problem just add if not there 
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children: # if character not in next level 
                node.children[char] = letter() # then add a letter node for it
            node = node.children[char] # now move the node down and keep going 
        node.end = True # mark node as the end of a word

    
    def search(self, word: str) -> bool:
        node = self.root
    
        def dfs(node, i): # we pass node and also i which is the index of the word 
            if i == len(word): # this is our base case where we return normally
                return node.end
            
            # handle a wildcard with recursive calls and check all children paths 
            if word[i] == '.':
                for kid in node.children.values(): # iterate through the values of children not just the keys lol
                    if dfs(kid, i+1): # if dfs returns true then we return true
                        return True
                return False  # if none of the paths return true then return false
            
            # handle a regular character 
            if word[i] not in node.children:
                return False 

            # go to next character if no one returned false 
            return dfs(node.children[word[i]], i + 1)

        return dfs(node, 0) #call dfs in recursive function 
