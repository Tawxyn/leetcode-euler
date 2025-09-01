#class Solution(object):
#    def majorityElement(self, nums):
#        count = {}
#
#        for i in range(len(nums)):
#            if nums[i] not in count:
#                count[nums[i]] = 0
#            count[nums[i]] += 1
#        
#        return max(count, key=count.get)

# Boyer–Moore Voting Algorithm, this is the optimal solution
class Solution(object):
    def majorityElement(self, nums):
        res, count = 0, 0

        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)
        return res
