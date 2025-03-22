# Solution for Leetcode problem 345. Reverse Vowels of a String


class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p1 = 0
        p2 = len(s) - 1

        s = list(s)

        while p1 < p2:
            p1_is_vowel = self.is_vowel(s[p1])
            p2_is_vowel = self.is_vowel(s[p2])

            if p1_is_vowel and p2_is_vowel:
                # Swap the characters
                aux = s[p1]

                s[p1] = s[p2]
                s[p2] = aux

                p1 += 1
                p2 -= 1

            elif p1_is_vowel:
                p2 -= 1

            elif p2_is_vowel:
                p1 += 1

            else:
                p1 += 1

        s = "".join(s)  # Convert back to string

        return s

    def is_vowel(self, c):
        return c.lower() in {'a', 'e', 'i', 'o', 'u'}
