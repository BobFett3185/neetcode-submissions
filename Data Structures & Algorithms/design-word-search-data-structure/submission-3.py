class letter:
    def __init__(self):
        self.children = {}
        self.end = False
    
class WordDictionary:
    def __init__(self): # make our tree here
        self.root = letter()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children: # if character not in next level 
                node.children[char] = letter() # then add a letter node for it
            node = node.children[char] # now move the node down and keep going 
        node.end = True

    
    def search(self, word: str) -> bool:
        node = self.root
    
        def dfs(node, i): # we pass node and also i which is the index of the word 
            if i == len(word):
                return node.end
            
            # handle a wildcard recursively 
            if word[i] == '.':
                for kid in node.children.values(): # iterate through the values of children not just the keys lol
                    if dfs(kid, i+1):
                        return True
                return False 
            
            # handle a regular character 
            if word[i] not in node.children:
                return False 

            # go to next character if no one returned false 
            return dfs(node.children[word[i]], i + 1)

        return dfs(node, 0) #call dfs in recursive function 
