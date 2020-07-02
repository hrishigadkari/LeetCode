class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        for i in range(0,len(board)):
            if ("R" in board[i]):
                row = i
        for i in range(0,len(board)):
            if ("R" == board[row][i]):
                col = i
        #print(col)
        hor = board[row]
        ver = []
        for i in range(0,len(board)):
            ver.append(board[i][col])
        hor = [x for x in hor if x != "."]
        ver = [x for x in ver if x != "."]
        c = 0
        for i in range(0,len(hor)-1):
            if ((hor[i] == 'p' and hor[i+1] == 'R') or (hor[i] == 'R' and hor[i+1] == 'p')):
                c += 1
        for i in range(0,len(ver)-1):
            if ((ver[i] == 'p' and ver[i+1] == 'R') or (ver[i] == 'R' and ver[i+1] == 'p')):
                c += 1
                
        return c