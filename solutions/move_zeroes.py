from utils.aux import measure_time


class Solution(object):
    @measure_time
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        f_zero_pos = -1
        #print(nums)

        if nums[0] == 0:
            f_zero_pos = 0

        for n in range(1, len(nums)):

            if nums[n] == 0 and f_zero_pos == -1:
                f_zero_pos = n

            if nums[n-1] == 0 and nums[n] != 0:
                nums[f_zero_pos] = nums[n]
                f_zero_pos += 1
                nums[n] = 0
                #print(nums)

        #print(nums)

        return None
