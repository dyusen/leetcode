class Solution:
    def isPalindrome(self, s: str) -> bool:
        start_pointer = 0
        end_pointer = len(s) - 1
        if len(s) == 1:
            return True

        while start_pointer <= end_pointer:
            if not s[start_pointer].isalnum():
                while start_pointer < end_pointer and not s[start_pointer].isalnum():
                    start_pointer += 1
            if not s[end_pointer].isalnum():
                while start_pointer < end_pointer and not s[end_pointer].isalnum():
                    end_pointer -= 1

            if s[start_pointer].isalpha() and s[start_pointer].isalpha() and s[start_pointer].lower() == s[
                end_pointer].lower():
                start_pointer += 1
                end_pointer -= 1
                continue
            elif s[start_pointer] == s[end_pointer]:
                start_pointer += 1
                end_pointer -= 1
                continue
            else:
                return False

        return True


s = Solution()
print(s.isPalindrome("123021"))
