## [80. Remove Duplicates from Sorted Array II](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150)

**Problem:**  
Given a sorted array `nums`, remove duplicates in-place such that **each element appears at most twice**. Return the new length `k`.  
- Must use **O(1)** extra space.  
- Relative order of elements should be preserved.  


### Intuition  
- Since the array is sorted, duplicates are **adjacent**.  
- Use **two pointers**:  
  - `i` → scans through the array  
  - `k` → position of next allowed element  
- Track a `count` of how many times the current element has appeared.  
- Only copy the element if `count <= 2`.  


### Complexity  
- **Time:** `O(n)` (single pass through array)  
- **Space:** `O(1)` (in-place)  

---
---

## [122. Best Time to Buy and Sell Stock II](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/?envType=study-plan-v2&envId=top-interview-150)

**Problem:**  
You are given an array `prices` where `prices[i]` is the price of a stock on day `i`.  
- You may complete as many transactions as you like (buy one and sell one share multiple times).  
- You must sell before you buy again.  
- Return the maximum profit you can achieve.

---

### Intuition  
- The key insight: every time the price goes **up** from one day to the next, you can take that profit.  
- Instead of trying to find local minima and maxima explicitly, just **sum up all positive differences**:  
  - If `prices[i] > prices[i-1]`, profit += `prices[i] - prices[i-1]`.  
- This greedy approach works because:  
  - Multiple small profitable moves (day-to-day increases) add up to the same result as waiting for the peak.  
  - Example: `[1, 2, 3]` → buy at 1, sell at 3 (profit 2), or take (1→2) + (2→3) = 2. Both yield the same maximum.  

---

### Complexity  
- **Time:** `O(n)` (single pass through array).  
- **Space:** `O(1)` (constant extra variables).  

---
---

# [55. Jump Game](https://leetcode.com/problems/jump-game/?envType=study-plan-v2&envId=top-interview-150)

**Problem:**  
You are given an integer array `nums` where each element `nums[i]` represents the maximum jump length from index `i`.  
- You start at index `0`.  
- Return `True` if you can reach the **last index**, otherwise `False`.

---

### Intuition  
- Use a **greedy approach**: track the **farthest index** you can reach so far.  
- Initialize `max_reach = 0`.  
- Iterate through the array:  
  1. If the current index `i` is greater than `max_reach`, you are **stuck** → return `False`.  
  2. Update `max_reach = max(max_reach, i + nums[i])`.  
  3. If `max_reach >= last_index`, you can already reach the end → return `True`.  
- If the loop finishes without getting stuck, return `True`.  

This works because at each index, you only need to know the farthest place reachable so far, not the exact jump path.

---
---
