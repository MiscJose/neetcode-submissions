class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_sorted = sorted(set(nums))
        if not nums:
            return 0

        res = 1
        count = 1
        for i in range(len(nums_sorted)-1):
            if nums_sorted[i+1] - nums_sorted[i] == 1:
                count+=1
                res = max(res, count)
            else:
                count=1
        
        return res