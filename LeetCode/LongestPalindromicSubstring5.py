class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(N^2)
        # odd pattern
        odd = []
        for i in range(len(s)):
            stride = 1
            while True:
                st = i-stride
                ed = i+stride
                if not (st>=0 and ed<len(s)): break
                if(s[st] == s[ed]): 
                    if stride == 1:
                        odd.append([i, 3])
                    odd[-1] = [i, 2*stride+1]
                else: break
                stride += 1
        # even pattern
        even = []
        for i in range(len(s)):
            stride = 1
            while True:
                st = i-stride+1
                ed = i+stride
                if not (st>=0 and ed<len(s)): break
                if(s[st] == s[ed]): 
                    if stride == 1:
                        even.append([i, 2])
                    even[-1] = [i, 2*stride]
                else: break
                stride += 1
        
        # find the longest palindrome substring
        maxno = 0
        cet = 0
        pat = -1
        for pr in odd:
            if(pr[1]>maxno):
                maxno = pr[1]
                cet = pr[0]
                pat = 1
        for pr in even:
            if(pr[1]>maxno):
                maxno = pr[1]
                cet = pr[0]
                pat = 0
        # generate substring answer
        # print(maxno, cet, pat, ", maxno, ceter, pattern")
        substr = ""
        if pat == 0:
            wing = int(maxno/2)
            for i in range(cet-wing+1, cet+wing+1):
                substr += s[i]
        else:
            wing = int((maxno-1)/2)
            for i in range(cet-wing, cet+wing+1):
                substr += s[i]
        return substr

def test_answer():
    S = Solution()
    ans = []
    ans.append(S.longestPalindrome("babad"))
    assert (ans[0] == "bab") or (ans[0] == "aba")
    assert S.longestPalindrome("cbbd") == "bb"
    assert S.longestPalindrome("bb") == "bb"
    assert S.longestPalindrome("aaaa") == "aaaa"

def debug():
    S = Solution()
    # S.longestPalindrome("babad")
    # S.longestPalindrome("bb")
    S.longestPalindrome("aaaa") == "aaaa"
debug()
        
        