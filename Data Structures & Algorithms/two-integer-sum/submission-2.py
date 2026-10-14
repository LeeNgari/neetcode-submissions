class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        store = {}

        for i in range(len(nums)):
            dist = target - nums[i]

            if dist in store:
                return [store[dist], i]
            
            store[nums[i]] = i
        