class Solution(object):
    def reverseWords(self, s):
        word_list = s.split()
        reverse_list = word_list[::-1]
        delimiter = ' '
        join_str = delimiter.join(reverse_list)
        return join_str
        