class Solution(object):
    def rotate(self, nums, k):

        def loop(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l, r = l + 1, r - 1

        k = k % len(nums)
        
        loop(0, len(nums) - 1)
        loop(0, k - 1)
        loop(k, len(nums) - 1)
