class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prods = [0] * len(nums)
        left_prods[1] = nums[0]
        right_prods = [0] * len(nums)
        right_prods[len(nums) - 2] = nums[-1]

        if len(nums) == 2:
            return [nums[1], nums[0]]

        for i in range(2, len(nums)):
            left_prods[i] = left_prods[i - 1] * nums[i - 1]
        
        for j in range(len(nums) - 3, -1, -1):
            right_prods[j] = right_prods[j + 1] * nums[j + 1]

        result = [0] * len(nums)
        result[0] = right_prods[0]
        result[-1] = left_prods[-1]

        for i in range(1, len(result) - 1):
            result[i] = left_prods[i] * right_prods[i]
        return result
        

        