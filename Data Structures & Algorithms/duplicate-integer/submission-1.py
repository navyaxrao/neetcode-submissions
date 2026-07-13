class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = set(nums)
        print(nums_set)
        if len(nums) == len(nums_set):
            return False
        return True

        