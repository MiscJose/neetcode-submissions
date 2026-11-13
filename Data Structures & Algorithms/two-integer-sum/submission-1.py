class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i in range(len(nums)):
            delta = target - nums[i]
            if delta in nums_dict:
                return [nums_dict[delta], i]
            nums_dict[nums[i]] = i
        
