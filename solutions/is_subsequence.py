class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        chars_found = 0
        s_size = len(s)

        if s == "":
            return True

        for character in t:
            if character == s[chars_found]:
                chars_found += 1

            if chars_found == s_size: 
                break

        if chars_found == s_size:
            return True

        else:
            return False
