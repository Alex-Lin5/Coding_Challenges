import time
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # O(N), Manacher's Algorithm
        # startt = time.time()
        spad = '#'+'#'.join(s)+'#' # might take a lot time overhead padding string
        rads = [0 for _ in range(len(spad))]
        rd = ct = maxr = maxc = 0
        # print(time.time() - startt)
        # startt = time.time()
        for i in range(1, len(spad)-1):
            # check palindrom within palindrom to save time
            # mirror = i-(i-ct)*2 = (ct-i)*2+i
            mirror = 2*ct-i
            if rd <= 1: pass
            elif i+rads[mirror] < ct+rd:
                rads[i] = rads[mirror]
                continue
            elif i+rads[mirror] >= ct+rd:
                rads[i] = ct+rd-i
            # print("step 1,", i, rads[i], ct, rd)
            # find out the max radius for this character
            while (i-rads[i]-1>=0 and i+rads[i]+1<len(spad) 
                and spad[i-rads[i]-1] == spad[i+rads[i]+1]):
                rads[i] += 1
            # move the radius and center if current one stays out of boundary
            if i >= ct+rd:
                ct = i
                rd = rads[i]
            # mark the largest radius and its center
            if rads[i] > maxr: 
                maxr = rads[i]
                maxc = i
        # print("radiuses,", rads, spad[maxc])
        # print(s, spad, '\n', maxc, maxr, ", center, radius")
        # print(time.time() - startt)
        if maxr<=1: return s[0]
        return s[(maxc-maxr)//2:(maxc+maxr)//2]

def test_answer():
    S = Solution()
    ans = []
    ans.append(S.longestPalindrome("babad"))
    assert (ans[0] == "bab") or (ans[0] == "aba")
    assert S.longestPalindrome("cbbd") == "bb"
    assert S.longestPalindrome("bb") == "bb"
    assert S.longestPalindrome("aaaa") == "aaaa"
    assert S.longestPalindrome("a") == "a"
    assert S.longestPalindrome("ab") == "a"
    assert S.longestPalindrome("def longestPalindrome(self, s: str) -> s") == "d"

def debug():
    S = Solution()
    # S.longestPalindrome("babad")
    # S.longestPalindrome("bb")
    # S.longestPalindrome("aaaa")
    S.longestPalindrome("def longestPalindrome(self, s: str) -> sngestPalindrome(self, s: str) -> sngestPalindrome(self, s: str) -> sngestPalindrome(self, s: str) -> sngestPalindrome(self, s: str) -> sngestPalindrome(self, s: str) -> sngestPalindrome(self, s: str) -> sngestPalindrome(self, s: str) -> sngestPalindrome(self, s: str) -> s")
debug()
        
        