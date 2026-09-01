class Solution(object):
    def minWindow(self, s, t):
        if not s or not t:
            return ""

        tmap = {}

        for c in t:
            tmap[c] = tmap.get(c, 0) + 1

        required = len(tmap)
        have = 0

        window = {}
        left = 0

        best_length = len(s) + 1
        best_left = 0

        for right in range(len(s)):
            c = s[right]

            if c in tmap:
                window[c] = window.get(c, 0) + 1

                if window[c] == tmap[c]:
                    have += 1

            while have == required:
                window_length = right - left + 1

                if window_length < best_length:
                    best_length = window_length
                    best_left = left

                left_char = s[left]

                if left_char in tmap:
                    window[left_char] -= 1

                    if window[left_char] < tmap[left_char]:
                        have -= 1

                left += 1

        if best_length == len(s) + 1:
            return ""

        return s[best_left:best_left + best_length]