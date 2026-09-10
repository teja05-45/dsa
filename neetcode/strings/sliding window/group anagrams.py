class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        hmap = {}
        for i in strs:
            sorted_word = ''.join(sorted(i))
            if sorted_word in hmap:
                hmap[sorted_word].append(i)
            else:
                hmap[sorted_word] = [i]
        return hmap.values()

#another solution using count of characters

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        res = defaultdict(list)

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            res[tuple(count)].append(s)

        return list(res.values())