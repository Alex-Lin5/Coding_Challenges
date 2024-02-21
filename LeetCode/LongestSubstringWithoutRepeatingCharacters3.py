class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hashset + DP, sliding window
        # Time O(N), Space O(1), size of hashset will not exceed the characters number 128
        if s == "": return 0
        chset = set()
        note = [1 for i in range(len(s))]
        left = 0
        for right in range(len(s)):
            while s[right] in chset:
                note[left] = len(chset)
                chset.remove(s[left])
                left += 1
                # print(right, left, chset)
            chset.add(s[right])            
        note[left] = len(chset)
        # print(note)
        return max(note)

def test_answer():
    S = Solution()
    assert S.lengthOfLongestSubstring("abcdaqwertba") == 9 # "cdaqwertb", duplicate two side
    assert S.lengthOfLongestSubstring("abcaaaaaacde") == 4 # "acde", duplicate middle
    assert S.lengthOfLongestSubstring("abcdcbal") == 5 # "dcbal", palindrome
    assert S.lengthOfLongestSubstring("abcaaaacdefb") == 6 # "acdefb", two frame
    assert S.lengthOfLongestSubstring("abcdabcd") == 4 # "abcd", second repeat
    assert S.lengthOfLongestSubstring("aaaabcdaef") == 6 # "bcdaef", sand in rice
    assert S.lengthOfLongestSubstring("") == 0 # empty

    assert S.lengthOfLongestSubstring("abcabcbb") == 3 # "abc"
    assert S.lengthOfLongestSubstring("bbbbbb") == 1 # "b", only one
    assert S.lengthOfLongestSubstring("pwwkew") == 3 # "wke"

def debug():
    S = Solution()
    S.lengthOfLongestSubstring("abcdaqwertba")

debug()
