class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        index = 0
        for num in nums:
            pair = target - num
            if pair in hmap:
                return [hmap[pair], index]
            hmap[num] = index
            index += 1
        return []



        