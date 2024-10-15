from find_peak_element import Solution


solution = Solution()


test_1 = [1, 2, 3, 1]
test_2 = [1,2,1,3,5,6,4]

print(f'Testcase {test_1}')
print(f'Expected 2')
print(solution.findPeakElement(test_1))

print(f'Testcase {test_2}')
print(f'Expected 5 or 1')
print(solution.findPeakElement(test_2))
