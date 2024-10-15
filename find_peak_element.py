class Solution(object):
    def findPeakElement(self, nums):
        
        size = len(nums)
        first_element = nums[0]
        last_element = nums[size-1]

        nums.insert(0, first_element-1)
        nums.append(last_element-1)

        #print(nums)

        i = 1
        while i < size+1:
            if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i-1

            i += 1

        return 0