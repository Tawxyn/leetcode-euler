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
