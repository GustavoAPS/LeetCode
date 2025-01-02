from utils.aux import measure_time


class Solution(object):
    @measure_time
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        operations = 0
        # print(f"Start:\n{nums}")

        flag = 0

        while flag == 0:
            flag = 1
            for n in range(1, len(nums)):
                if nums[n-1] == 0 and nums[n] != 0:
                    operations += 1
                    nums[n-1] = nums[n]
                    nums[n] = 0
                    # print(nums)
                    flag = 0

        # print(f"End: {nums}")

        # print(f'{operations} performed')

        return None
