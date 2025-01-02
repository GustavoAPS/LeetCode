from solutions.kids_with_candies import Solution

solution = Solution()


def test_1_kids_with_candies():
    assert solution.kidsWithCandies(candies=[2, 3, 5, 1, 3], extraCandies=3) == [True, True, True, False, True]


def test_2_kids_with_candies():
    assert solution.kidsWithCandies(candies=[4,2,1,1,2], extraCandies=1) == [True, False, False, False, False]

