class Solution(object):
    def majorityElement(self, nums):
        count = {}

        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 0
            count[nums[i]] += 1
        
        return max(count, key=count.get)
