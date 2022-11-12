class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list = {}
        
       
        for i , num in enumerate(nums):
            compliment = target - num 
            
            if compliment in list:
                return (list[compliment], i)
            
            list[num] = i