class Solution {
    public int triangleNumber(int[] nums) {
        Arrays.sort(nums);
        int ans=0;
        int last_index=nums.length-1;

        while(last_index>1)
        {
            int start=0,end=last_index-1;
            while(start<end)
            {
                if((nums[start]+nums[end])>nums[last_index])
                {
                    ans+=end-start;
                    end-=1;
                }
                else
                {
                    start+=1;
                }
            }
            last_index-=1;
        }
        return ans;
    }
}
