from solutions.solution_643 import Solution

solution = Solution()


def test_1():
    nums = [1, 12, -5, -6, 50, 3]
    k = 4
    output = 12.75
    assert solution.findMaxAverage(nums, k) == output


def test_2():
    nums = [5]
    k = 1
    output = 5.00000
    assert solution.findMaxAverage(nums, k) == output
