class Solution(object):
    def shiftingLetters(self, s, shifts):
        shift=sum(shifts)
        ans=''

        for i in range(len(s)):
            ans+=chr((ord(s[i])-97+shift)%26 +97)
            shift-=shifts[i]
        return ans
