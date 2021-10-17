from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx = 0
        for i in nums:
            find_data = target - i
            idx += 1
            if find_data in nums[idx:]:
                return [idx-1,nums[idx:].index(find_data)+idx]

		
print(Solution().twoSum([4,5,0,6,7,0], 0))

# 542 7