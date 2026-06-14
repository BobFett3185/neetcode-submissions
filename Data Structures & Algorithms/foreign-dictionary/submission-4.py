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
        visit = {} # false = visited # true in our path 
        res = []


        def dfs(c):
            if c in visit: # if its in visited 
                return visit[c]
                
            visit[c] = True

            for n in adj[c]:
                if dfs(n):
                    return True

            visit[c] = False 
            res.append(c)
                

        for c in adj:
            if dfs(c):
                return ""
        res.reverse()
        return "".join(res)
                
