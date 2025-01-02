def two_sum(arr, target):
    arr.sort()

    left = 0
    right = len(arr) - 1

    while left < right:
        sum = arr[left] + arr[right]

        if sum == target:
            return True
        elif sum < target:
            left += 1
        else:
            right -= 1

    return False


arr = [0, -1, 2, -3, 1]
target = -2

if two_sum(arr, target):
    print("true")
else:
    print("false")
