class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_count = defaultdict(int)

        for num in nums:
            nums_count[num]+=1
        
        nums_count_sorted = sorted(nums_count.items(),key=lambda x: x[1])
        nums_sorted = [x for x,y in nums_count_sorted]

        return nums_sorted[len(nums_sorted)-k:]
    
        

