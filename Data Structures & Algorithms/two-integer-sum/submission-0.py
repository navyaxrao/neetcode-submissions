class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range(len(nums)):
            num = nums[i]
            pair = target - num
            if pair in hmap:
                return [min(hmap[pair], i), max(hmap[pair], i)]
            hmap[num] = i
        return []

        