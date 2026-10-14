class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hash={}

        for index,val in enumerate(nums):
            diff = target - val

            if diff in hash:
                return [hash[diff], index ]

            hash[val] = index