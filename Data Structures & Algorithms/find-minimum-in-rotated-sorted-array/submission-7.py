class Solution:
    def findMin(self, nums: List[int]) -> int:

        # simpler standard solution
        # if len(nums) == 1:
        #     return nums[0]
        # left = 0
        # right = len(nums) - 1
        # middle = (left + right) // 2
        # while left < right:
        #     if nums[left] <= nums[middle]:
        #         left = middle + 1
        #     else:
        #         right = middle
        #     middle = (left + right) // 2
        # return nums[left]

        left, right = 0, len(nums) - 1

        while left < right:
            middle = (left + right) // 2

            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle

        return nums[left]


        # my solution
        # if not nums:
        #     return -1
        # if len(nums) == 1:
        #     return nums[0]
        # left = 0
        # right = len(nums) - 1
        # middle = (left + right) // 2
        # if nums[left] < nums[middle] < nums[right]:
        #     return nums[0]
        
        # while left <= right:
        #     print("left: " + str(left))
        #     print("right: " + str(right))
        #     print("middle: " + str(middle))
        #     if middle == 0:
        #         return min(nums[middle], nums[middle + 1])
        #     if middle == len(nums) - 1:
        #         return min(nums[middle - 1], nums[middle])
        #     if nums[middle - 1] > nums[middle] < nums[middle + 1]:
        #         return nums[middle]
        #     if nums[left] <= nums[middle]:
        #         if nums[middle] <= nums[right]:
        #             return nums[left]
        #         left = middle + 1
        #     else:
        #         right = middle - 1
        #     middle = (left + right) // 2
        
