from solutions.solution_345 import Solution

solution = Solution()


def test_1():
    input = "IceCreAm"
    output = "AceCreIm"
    assert solution.reverseVowels(input) == output


def test_2():
    input = "leetcode"
    output = "leotcede"
    assert solution.reverseVowels(input) == output
