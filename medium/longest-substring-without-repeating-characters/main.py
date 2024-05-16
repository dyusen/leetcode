class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        substring = set()
        res = 0
        while end < len(s):  # pwwkew
            if s[end] not in substring:
                substring.add(s[end])
            else:
                while s[end] in substring:
                    substring.remove(s[start])
                    start += 1
                substring.add(s[end])

            res = max(res, len(substring))
            end += 1

        return res
    # for start in range(len(s)):


r = Solution()
print(r.lengthOfLongestSubstring(s="pwwkew"), 3)
