from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums_counter = Counter(nums)
        for k, v in nums_counter.items():
            if v > len(nums) // 2:
                return k