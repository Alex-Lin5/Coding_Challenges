from typing import List
import pytest

class Solution:
    def nextPermutation(self, nums: List[int]) -> List[int]:
        bpv = 0
        bpp = -1
        for idx in range(len(nums)-1, 1, -1):
            # already in ascending order on the bottom part
            if(nums[idx]<=nums[idx-1]): continue
            bpp = idx-1
            bpv = nums[idx-1]
            break
        if(bpp == -1): 
            nums.reverse()
            return nums
        nov = 2**63
        nop = -1
        for idx in range(len(nums)-1, bpp, -1):    
            # mark smallest number and index after break point
            if(nums[idx]<nov and nums[idx]>bpv):
                nov = nums[idx]
                nop = idx
                break
        nums[nop], nums[bpp] = nums[bpp], nums[nop]
        if(bpp+1<len(nums)-1):
            tail = nums[bpp+1:]
            tail.reverse()
            nums[bpp+1:] = tail
            # nums[bpp+1:].reverse() # wrong code
        print(bpv, bpp, nov, nop)
        return nums

def test_answer():
    S = Solution()
    assert S.nextPermutation([1,2,3]) == [1,3,2]
    assert S.nextPermutation([3,2,1]) == [1,2,3]
    assert S.nextPermutation([1,3,2]) == [2,1,3]
    assert S.nextPermutation([4,3,2,5,1,3]) == [4,3,2,5,3,1]
    assert S.nextPermutation([4,3,2,5,3,1]) == [4,3,3,1,2,5]

test_answer()

# For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
# 4325 13 -> 43 2531 -> 43 3125
        