class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair=zip(position,speed)

        st=[]
        cur_time=0
        ans=0

        for p,s in reversed(sorted(pair)):
            t=(target-p)/s
            if t>cur_time:
                ans+=1
                cur_time=t
        return ans
