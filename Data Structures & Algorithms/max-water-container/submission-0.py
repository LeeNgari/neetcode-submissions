class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l,r =  0, len(heights) -1
        max_h=0

        while l<r:
            area = (r-l) * min(heights[l], heights[r])
            max_h = max(max_h,area)

            if heights[l] > heights[r]:
                r-=1
            else:
                l+=1

        return max_h

