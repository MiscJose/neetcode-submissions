class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0
            
        nums_set = set(nums)
        
        res = 1
        count = 0
        for num in nums:
            if num-1 not in nums_set:
                count=1
                temp = num
                while temp+1 in nums_set:
                    count+=1
                    temp+=1
                    res = max(res, count)
        
        return res

            