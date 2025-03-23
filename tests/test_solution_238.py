from solutions.solution_238 import Solution

solution = Solution()


def test_1():
    input = [2, 3, 4]
    output = [12, 8, 6]
    assert solution.productExceptSelf(input) == output


def test_2():
    input = [1, 2, 3, 4]
    output = [24, 12, 8, 6]
    assert solution.productExceptSelf(input) == output


def test_3():
    input = [-1, 1, 0, -3, 3]
    output = [0, 0, 9, 0, 0]
    assert solution.productExceptSelf(input) == output
