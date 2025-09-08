class Solution(object):
    def canJump(self, nums):
        max_reach = 0
        last = len(nums) - 1

        for i, step in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + step)
            if max_reach >= last:
                return True

        return True
