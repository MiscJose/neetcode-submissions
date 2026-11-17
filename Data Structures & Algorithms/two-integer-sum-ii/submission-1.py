class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            diff = target-numbers[i]
            R = len(numbers)-1
            L=i+1
            while L<=R:
                M = (L+R) // 2
                if numbers[M] == diff:
                    return [i+1, M+1]
                elif numbers[M] < diff:
                    L = M+1
                else:
                    R = M-1
        
        return []
