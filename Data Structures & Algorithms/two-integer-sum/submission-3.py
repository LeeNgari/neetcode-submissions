class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        prevMap = {}

        for i,number in enumerate(nums):
            difference = target - number

            if difference in prevMap:
                return [prevMap[difference], i]

            prevMap[number] = i