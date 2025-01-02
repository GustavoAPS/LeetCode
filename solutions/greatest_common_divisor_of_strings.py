class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        # Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
        # For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t 
        # (i.e., t is concatenated with itself one or more times).

        t = ''
        smallest = min(len(str1), len(str2))

        for n in range(0, smallest):
            # print(f'{str1[n]} {str2[n]}')
            if str1[n] == str2[n]:
                t += str1[n]

        divisors = self.find_divisors(len(t))

        t_reduced = ''

        for n in divisors:
            lst = self.split_into_groups(t, n)
            # print(lst)
            if len(set(lst)) == 1:
                t_reduced = lst[0]
                break

        if len(str2) < len(str1):
            if self.is_repeated_pattern(str1):
                return t_reduced

        if len(str2) > len(str1):
            if self.is_repeated_pattern(str2):
                return t_reduced

        else:
            return ""

    def is_repeated_pattern(self, s):
        length = len(s)
        for i in range(1, length // 2 + 1):
            if length % i == 0:  # O comprimento da string é múltiplo do comprimento do padrão
                if s[:i] * (length // i) == s:
                    return True
        return False

    def split_into_groups(self, s, n):
        return [s[i:i + n] for i in range(0, len(s), n)]

    def find_divisors(self, n):
        divisors = []
        for i in range(1, n + 1):
            if n % i == 0:
                divisors.append(i)
        return divisors
