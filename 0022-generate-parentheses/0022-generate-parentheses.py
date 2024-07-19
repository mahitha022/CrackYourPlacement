class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        l=[]
        def para(open,close,s):
            if(open==n and close==n):
                l.append(s)
                return 
            if(open<=n):
                para(open+1,close,s+'(')
            if(open>close):
                para(open,close+1,s+')')
            return
        para(0,0,"")
        return l