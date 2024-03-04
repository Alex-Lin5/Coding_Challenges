from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Brutal force, find out all possible rectangle area from any 2 points
        # Time O(N^2), Space O(N)

        # Monotonous Stack
        # Time O(3N)->O(2N), Space O(2N)->O(N), could be optimized
        maxh = 0
        inc = [-1 for _ in range(len(heights))]
        dec = [-1 for _ in range(len(heights))]
        stk = [-1]
        for i in range(len(heights)):
            # \ from left to right remove blocks with greater heights than current one
            while stk[-1]!=-1 and heights[stk[-1]]>=heights[i]:
                stk.pop()
            inc[i] = stk[-1]
            stk.append(i)
        stk = [-1]
        for i in range(len(heights)-1, -1, -1):
            # / from right to left remove blocks with greater heights than current one
            while stk[-1]!=-1 and heights[stk[-1]]>=heights[i]:
                stk.pop()
            dec[i] = stk[-1]
            stk.append(i)
        for i in range(len(heights)):
            if dec[i] == -1: dec[i] = len(heights)
            ht = heights[i]
            wd = dec[i]-inc[i]-1
            # \___/, compare the largest area with current height multiply corresponding max width
            maxh = max(maxh, wd*ht)
        print(inc, dec, heights)
        return maxh
    
def test_answer():
    S = Solution()
    assert S.largestRectangleArea([0]) == 0
    assert S.largestRectangleArea([2,4]) == 4
    assert S.largestRectangleArea([2,1,5,6,2,3]) == 10

def debug():
    S = Solution()
    S.largestRectangleArea([0])

debug()