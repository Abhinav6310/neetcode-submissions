class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        a[nums[0]] = 0

        for i in range(1,len(nums)):
            try:
                return [a[target-nums[i]],i]
            except:
                a[nums[i]] = i
        return -1