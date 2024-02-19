class Solution:
    def minWindow(self, S:str, T:str) -> str:
        # iterate through big string, push the index when first character matched
        # keep counting the length of substring, and mark another index that matched the first character
        # note down the whole substring by beginning index and length, continue searching on another beginning until end of string
        # at last, find the shortest substring with smallest starting index
        # Time O(S^2), Space O(S)
        
        # Dynamic Programing
        # Time O(ST), Space O(ST)
        dp = [[-1 for t in range(len(T))] for s in range(len(S))] # dp[s][t]
        for i in range(len(S)):
            if(S[i] == T[0]):
                dp[i][0] = i
            elif(i != 0):
                dp[i][0] = dp[i-1][0]
        for j in range(1, len(T)):
            for i in range(j, len(S)):
                if S[i] == T[j]:
                    dp[i][j] = dp[i][j-1]
                else:
                    dp[i][j] = dp[i-1][j]

        st = -1; ln = len(S)
        for i in range(len(T)-1, len(S)):
            if dp[i][len(T)-1] != -1:
                lntp = i-dp[i][len(T)-1]+1
                if lntp < ln:
                    ln = lntp
                    st = dp[i][len(T)-1]
        # print(len(dp), len(dp[0]))
        # print(S, T, '\n', dp)
        # print(st, ln)
        if st == -1:
            return ""
        return S[st:st+ln]

def test_answer():
    S = Solution()
    assert S.minWindow("abcdebdde", "bde") == "bcde"
    assert S.minWindow("abccadefde", "cde") == "cade"
    assert S.minWindow("abccadddefde", "cdde") == "caddde"
    assert S.minWindow("abcdnnifchdfisg", "cdf") == "chdf"
    assert S.minWindow("aaclclldlcldllc", "cdc") == "clldlc"
    assert S.minWindow("bababbbbbaaaaacc", "bac") == "baaaaac"

def debug():
    S = Solution()
    S.minWindow("abcdebdde", "bde")

debug()