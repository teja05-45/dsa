class Solution(object):
    def totalFruit(self, fruits):
        count = {}
        left = 0
        max_count = 0

        for right in range(len(fruits)):
            count[fruits[right]] = count.get(fruits[right], 0) + 1

            while len(count) > 2:
                count[fruits[left]] -= 1

                if count[fruits[left]] == 0:
                    del count[fruits[left]]

                left += 1

            max_count = max(max_count, right - left + 1)

        return max_count