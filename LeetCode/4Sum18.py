from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        # print(nums)
        result = set()
        for i in range(0, len(nums)-3):
            for j in range(i+1, len(nums)-2):
                low = j+1
                high = len(nums)-1
                while low < high:
                    # print(i, j, low, high)
                    if(nums[i]+nums[j]+nums[low]+nums[high] == target):
                        result.add(tuple([nums[i], nums[j], nums[low], nums[high]]))
                        # print("added, ", nums[i], nums[j], nums[low], nums[high])
                    if(nums[i]+nums[j]+nums[low]+nums[high] > target):
                        high -= 1
                    elif(nums[i]+nums[j]+nums[low]+nums[high] < target):
                        low += 1
                    else: low += 1
        return [list(pr) for pr in result]
        # return sorted([list(pr) for pr in result])

inp = []
inp.append([1,0,-1,0,-2,2])
inp.append([2,2,2,2,2])
inp.append([-2,-1,-1,1,1,2,2])
ans = []
ans.append([[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]])
ans.append([[2,2,2,2]])
ans.append([[-2,-1,1,2],[-1,-1,1,1]])

def test_answer():
    S = Solution()
    assert S.fourSum(inp[0], 0) == ans[0]
    assert S.fourSum(inp[1], 8) == ans[1]
    assert S.fourSum(inp[2], 0) == ans[2]
                
def debug():
    S = Solution()
    # print("result, ", S.fourSum(inp[0], 0))
    # print("answer, ", ans[0])
    # print("result, ", S.fourSum(inp[1], 8))
    # print("answer, ", ans[1])
    print("result, ", S.fourSum(inp[2], 0))
    print("answer, ", ans[2])
debug()