class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # create two pointers, calculate max of len x height

        max_water = 0

        L, R = 0, len(heights)-1

        while L<R:
            length = R-L
            height = min(heights[L], heights[R])
            max_water = max(max_water, length*height)

            if heights[L] < heights[R]:
                L+=1
            else:
                R-=1
        
        return max_water