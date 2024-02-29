from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Time O(N), Space O(1) required
        # swap the original list so that it starts with 1, 2, ..., n
        # the first unmatched number in slot is the missing positive

        # lt = 0; rt = len(nums)-1
        # while lt <= rt :
        #     val = nums[lt]
        #     # swap and move right cursor to the left if value outbounded from [1,n] or remaining slots number
        #     if val == lt+1:
        #         lt += 1
        #     elif val < 1 or val > rt+1:
        #         nums[lt], nums[rt] = nums[rt], nums[lt]
        #         rt -= 1
        #     # swap the current value in left cursor to correct slot
        #     elif val != lt+1:
        #         if nums[lt] == nums[val-1]: lt += 1
        #         else:
        #             nums[lt], nums[val-1] = nums[val-1], nums[lt]
        # # print(lt, rt, '\n', nums)
        # for i in range(len(nums)):
        #     if i != nums[i]-1: return i+1
        # return len(nums)+1
    
        for i in range(len(nums)):
            # swap if correct value nums[i] is not in slot nums[i]-1
            while nums[i]>0 and nums[i]<=len(nums) and nums[nums[i]-1] != nums[i]:
                # print(i, nums[i], '\n', nums)
                val = nums[i]
                nums[i], nums[val-1] = nums[val-1], nums[i]
        for i in range(len(nums)):
            if i != nums[i]-1: return i+1
        return len(nums)+1

def test_answer():
    S = Solution()
    assert S.firstMissingPositive([1,2,2,1,3,1,0,4,0]) == 5
    assert S.firstMissingPositive([3,1,3]) == 2
    assert S.firstMissingPositive([2,2]) == 1
    assert S.firstMissingPositive([2,1]) == 3
    assert S.firstMissingPositive([1]) == 2
    assert S.firstMissingPositive([1,2,3]) == 4
    assert S.firstMissingPositive([1,2,0]) == 3
    assert S.firstMissingPositive([3,4,-1,1]) == 2
    assert S.firstMissingPositive([7,8,9,11,12]) == 1

def debug():
    S = Solution()
    S.firstMissingPositive([3,4,-1,1])

debug()