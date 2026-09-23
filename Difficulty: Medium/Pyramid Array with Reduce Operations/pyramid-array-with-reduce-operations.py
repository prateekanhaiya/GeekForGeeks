class Solution:
    def formPyramid(self, arr):
        n = len(arr)

        left = [0] * n
        right = [0] * n

        left[0] = 1

        for i in range(1, n):
            left[i] = min(arr[i], left[i - 1] + 1)

        right[n - 1] = 1

        for i in range(n - 2, -1, -1):
            right[i] = min(arr[i], right[i + 1] + 1)

        max_height = 0

        for i in range(n):
            max_height = max(max_height, min(left[i], right[i]))

        kept = max_height * max_height

        return sum(arr) - kept