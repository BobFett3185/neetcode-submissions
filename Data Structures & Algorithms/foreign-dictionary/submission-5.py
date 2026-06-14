class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        '''
        Go through each pair of adjacent words and find the first differing character 
        that is a rule you can represent as a edge on a directed graph 

        Once you build the graph you can check if there are no cycles bc there can 
        be no cycles due to their needing to be a strict sequential ordering of them 

        You need to do a post order dfs which adds the node last 
        goes through then processes element 


        '''
        adj = {c: set() for w in words for c in w}

        for i in range(len(words)-1): # go through the words 
            w1 = words[i]
            w2 = words[i+1]
            minlen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minlen] == w2[:minlen]: #  impossible case
                return ""

            for j in range(minlen): # go through the characters of the words
                if w1[j] != w2[j]: # when we find a different character
                    adj[w1[j]].add(w2[j]) # make an edge from 1 to 2
                    break 

        # now we go through our graph we made 
        visit = {} # false = visited   true means in our path 
        res = []

# keep track of if its on path and if all its children have been explored

        def findCycle(c):
            if c in visit: # if its in visited 
                return visit[c] # if we have alr visited on our path its returning true
                #if we have finished processing its false , can skip its children bc its all good 
                
            visit[c] = True # set to true to put it on our path

            for n in adj[c]: # for all the neighbors explore them
                if findCycle(n): # if we return true (node on our path )
                    return True # then its a cycle so return true

            # if we get here then no children were causing a cycle
            visit[c] = False  # set it to false, as all its children have been processed
            res.append(c) # append node to our result list at the end bc its all good
            

        for c in adj:
            if findCycle(c): # if we return true then we found a cycle 
                return ""
        res.reverse() # since we build backward we reverse and return 
        # we build this backwards and only append it after it reaches a dead end and others have been added first 
        
        return "".join(res)
                
