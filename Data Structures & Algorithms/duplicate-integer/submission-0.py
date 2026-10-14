class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        hashMap={}

        truth = False
        for index, item in enumerate(nums):
            if item in hashMap:
                truth = True
            else:
                hashMap[item] = index  
        
        return truth