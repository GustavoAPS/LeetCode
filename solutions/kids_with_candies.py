class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """

        return_list = []

        greater_amount = -1

        for kid in candies:
            if kid >= greater_amount:
                greater_amount = kid

        for kid in candies:
            if (kid + extraCandies) >= greater_amount:
                return_list.append(True)
            else:
                return_list.append(False)

        return return_list 
