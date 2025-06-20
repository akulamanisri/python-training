class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_map = {}  
        for i in range(len(nums)):
            frst = target - nums[i]
            if frst in num_map:
                return [num_map[frst], i]
            num_map[nums[i]] = i
