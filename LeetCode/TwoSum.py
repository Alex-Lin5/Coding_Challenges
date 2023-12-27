nums = [2,7,11,15]
target = 9

class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    sumDict = dict()
    index = 0
    for num in nums:
      if(target-num in sumDict):
        num1 = index
        num2 = sumDict.get(target-num)
        return num1, num2
      else:
        sumDict[num] = index
      index += 1

S = Solution();
print(S.twoSum(nums, target))
