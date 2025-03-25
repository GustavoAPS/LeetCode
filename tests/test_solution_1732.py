from solutions.solution_1732 import Solution

solution = Solution()


def test_1():
    gain = [-5, 1, 5, 0, -7]
    output = 1
    assert solution.largestAltitude(gain) == output


def test_2():
    gain = [-4, -3, -2, -1, 4, 3, 2]
    output = 0
    assert solution.largestAltitude(gain) == output
