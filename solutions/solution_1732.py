class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """

        max_altitude = 0
        current_altitude = 0

        for n in gain:
            current_altitude += n
            if current_altitude > max_altitude:
                max_altitude = current_altitude

        return max_altitude
