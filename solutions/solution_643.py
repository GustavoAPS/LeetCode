class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """

        sliding_sum = 0

        # print("\n")

        initial_sum = 0

        # Calculate initial average
        for n in range(0, k):
            initial_sum += nums[n]

        sliding_sum = initial_sum

        # Set the initial average to be the Max
        max_average = initial_sum / float(k)

        # 0 to k - 1 is covered in the first pass
        window_start_index = 1
        window_end_index = k

        # print(f"{window_start_index}-{window_end_index}")

        while window_end_index < len(nums):

            # print(f"Before {sliding_sum}")

            sliding_sum -= nums[window_start_index-1]
            # print(f"Subtracting {nums[window_start_index-1]}")

            sliding_sum += nums[window_end_index]
            # print(f"Adding {nums[window_end_index]}")

            # print(f"Current sum is {sliding_sum}")

            if (sliding_sum / float(k)) > max_average:
                max_average = sliding_sum / float(k)

            window_start_index += 1
            window_end_index += 1

        return max_average
