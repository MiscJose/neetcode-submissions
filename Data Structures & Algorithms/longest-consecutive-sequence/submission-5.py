class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums_set = set(nums)
        
        res = 1
        for num in nums:
            if num-1 not in nums_set:
                count=1
                while num+count in nums_set:
                    count+=1
                    res = max(res, count)
        
        return res

            