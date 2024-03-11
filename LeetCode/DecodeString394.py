class Solution:
    def decodeString(self, s: str) -> str:
        # Time O(k*N), where k is the number of embbeded layer, Space O(1+N)
        ans = ""
        spt = ""
        flag = ""
        lt = len(s); rt = 0
        # only hold values in the number of embbeded layer
        stkl = []; stkr = []
        for i in range(len(s)):
            flag = "no"
            if s[i] == '[': 
                flag = "lt"
                stkl.append(i)
            elif s[i] == ']':
                stkr.append(i)
                if len(stkl)-len(stkr)>=2: continue
                tp = 0
                while True:
                    tp = stkl.pop()
                    if len(stkl)<2: break
                    
                lt = tp-1
                while True:
                    if s[lt].isnumeric(): lt -= 1
                    else: break
                lt += 1
                rt = stkr.pop()
                if len(stkl)>0:
                    # embedded coding string
                    flag = "em"
                    ss = s[lt:rt+1]
                    print(i, ss)
                    stp = Solution().decodeString(ss)
                    spt += stp
                elif len(stkl)==0:
                    # flat coding string
                    flag = "plain"
                    ntp = int(s[lt:tp])
                    ans += ntp*spt
                    spt = ""
            elif s[i].isnumeric():
                flag = "num"
            # Uncoded character
            elif not s[i].isnumeric(): 
                flag = "char"
                if len(stkl)==1: 
                    spt += s[i]
                elif len(stkl)==0: ans += s[i]
            print(i, s[i], flag, stkl, stkr, spt, ans)
        return ans
                    
def test_answer():
    S = Solution()
    assert S.decodeString("3[a]2[bc]") == "aaabcbc"
    assert S.decodeString("3[a2[c]]") == "accaccacc"
    assert S.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"
    assert S.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef") == "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"

def debug():
    S = Solution()
    # S.decodeString("3[a]2[bc]")
    # S.decodeString("3[a2[c]]")
    S.decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef")

debug()