class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        largest_area = 0

        # print(f'Container has {len(height)} lines')

        for i in range(0, len(height)):
            for j in range(i+1, len(height)):
                distance = j-i
                area = min(height[i], height[j]) * distance
                if area >= largest_area:
                    largest_area = area
                # print(f"Comparing from {height[i]} to {height[j]}, distance is {distance}, area is: { area }")

            # print('\n')

        return largest_area
