class Tnode: # create a prexit tree node
    def __init__(self):
        self.children= {}
        self.end = False
    def addWord(self, word):
        node = self 
        for c in word:
            if c not in node.children:
                node.children[c] = Tnode()
            node = node.children[c]
        node.end = True
    

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    
        root = Tnode()
        for w in words: # ADD all to words to our prefix tree
            root.addWord(w)
        
        ROWS, COLS = len(board), len(board[0])
        res = set() # result set can't return duplicates
        visit = set() # visited set, can't include same character twice 

        def dfs(r, c, node, word):
            if (r<0 or c <0 or r==ROWS or c == COLS or (r,c) in visit or
                board[r][c] not in node.children):
                return

            # otherwise the letter is there in the board and in the tree
            visit.add((r,c))# so we add the pair to visit
            node = node.children[board[r][c]] # we move to the next node 

            # if we reached the end of a word we add it to the list
            if node.end: 
                res.add(word+board[r][c])

            # then we keep going and call dfs on all the directions 
            dfs(r+1,c, node, word+board[r][c])
            dfs(r-1,c, node, word+board[r][c])
            dfs(r,c+1, node, word+board[r][c])
            dfs(r,c-1, node, word+board[r][c])

            visit.remove((r,c))

        for r in range(ROWS):
            for c in range(COLS):
                dfs(r,c,root,"")

        return list(res)

