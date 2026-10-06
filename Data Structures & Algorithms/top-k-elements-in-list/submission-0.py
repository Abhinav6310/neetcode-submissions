import collections
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_cou = collections.Counter(nums)
        buck_length = len(nums)+1
        buckets = [[] for i in range(buck_length)]
        for i in val_cou.keys():
            buckets[val_cou[i]].append(i)
        ans = []
        for i in range(buck_length-1,-1,-1):
            for j in buckets[i]:
                ans.append(j)
            k = k-len(buckets[i])
            if k<=0:
                break
        return ans
        
        