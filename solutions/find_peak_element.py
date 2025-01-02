class Solution(object):
    def findPeakElement(self, nums):
        low = 0
        high = len(nums) - 1
        
        while low <= high:

            mid = low + (high - low) // 2

            # print(f'Looking from {low} to {high}')
            # print(f'array: {nums} where mid is {mid}')
            left_value = -1
            right_value = -1

            if (mid - 1) < 0:
                left_value = nums[mid] - 1
            else: 
                left_value = nums[mid-1]

            if (mid + 1) > len(nums) - 1:
                right_value = nums[mid] - 1
            else: 
                right_value = nums[mid + 1]

            if left_value < nums[mid] and right_value < nums[mid]:
                # print(f'peak is {nums[mid]}')
                return mid

            elif nums[mid + 1] > nums[mid]:
                low = mid + 1

            else:
                high = mid - 1

        return -1
