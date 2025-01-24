class Solution(object):
    def convert(self, s, numRows):
        if numRows==1:
            return s

        st=['']*numRows
        goingDown=False
        currentRow=0

        for ch in s:
            st[currentRow]+=ch
            if currentRow==0:
                goingDown=True
            if currentRow==numRows-1:
                goingDown=False
            
            if goingDown:
                currentRow+=1
            else:
                currentRow-=1
        return "".join(st) 
