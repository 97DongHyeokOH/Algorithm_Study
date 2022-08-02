class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_set = set([i for i in range(1, len(nums)+1)])
        num_set -= set(nums)
        
        if num_set:
            return min(num_set)
        return max(nums)+1