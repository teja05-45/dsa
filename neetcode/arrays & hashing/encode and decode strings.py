class Solution:

    def encode(self, strs):
        result = ""

        for s in strs:
            result += str(len(s)) + "#" + s

        return result

    def decode(self, s):
        result = []
        i = 0

        while i < len(s):
            j = i

            # Find #
            while s[j] != "#":
                j += 1

            # Get length
            length = int(s[i:j])

            # Get the actual string
            word = s[j + 1 : j + 1 + length]
            result.append(word)

            # Move to next encoded string
            i = j + 1 + length

        return result


obj = Solution()
print(obj.encode(["hello", "world"]))
print(obj.decode("5#hello5#world"))
