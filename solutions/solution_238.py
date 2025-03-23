class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        # print("\n")

        reversed_nums = nums[::-1]

        first_to_last = []
        last_to_first = []
        result = []

        first_to_last.append(nums[0])
        last_to_first.append(nums[len(nums) - 1])

        for i in range(1, len(nums)):
            first_to_last.append(first_to_last[i-1]*nums[i])

        for i in range(1, len(reversed_nums)):
            last_to_first.append(last_to_first[i-1]*reversed_nums[i])

        last_to_first = last_to_first[::-1]

        for i in range(0, len(nums)):

            if i == 0:
                # print(f"Element [{i}] = last to first[{i+1}]")
                result.append(last_to_first[i+1])

            elif i == len(nums) - 1:
                # print(f"Element [{i}] = first to last[{len(nums)-2}]")
                result.append(first_to_last[len(nums)-2])

            else:
                # print(f"Element [{i}] = First to last [{i-1}]{first_to_last[i-1]} * Last to first [{i}]{last_to_first[i+1]}")

                result.append(first_to_last[i-1] * last_to_first[i+1])

        # print("\n")
        # print(f"Original array: {nums}")

        # i is all the previous values multiplied (inclusive)
        # print(f"First to last:  {first_to_last}")

        # i is all the next i values multiplied
        # print(f"Last to first:  {last_to_first}")

        # print(f"Result:         {result}")

        # First to last Order
        # [0]1, [1]2, [2]6, [3]24

        # Last to first order
        # [0]4, [1]4*3, [2]4*3*2, [3]4*3*2*1

        return result
