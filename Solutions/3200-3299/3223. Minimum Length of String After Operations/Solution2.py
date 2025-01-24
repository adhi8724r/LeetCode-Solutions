class Solution(object):
    def minimumLength(self, s):
        d={}
        for i in s:
            d[i]=d.get(i,0)+1

        ans=0
        for k in d.values():
            if k%2==0:
                ans+=2
            else:
                ans+=1
        return ans
