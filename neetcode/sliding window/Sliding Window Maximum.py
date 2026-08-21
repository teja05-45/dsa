from collections import deque

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        result = []

        for right in range(len(nums)):

            # Remove smaller elements
            while dq and nums[dq[-1]] <= nums[right]:
                dq.pop()

            dq.append(right)

            # Remove elements outside the window
            if dq[0] <= right - k:
                dq.popleft()

            # Window has reached size k
            if right >= k - 1:
                result.append(nums[dq[0]])

        return result