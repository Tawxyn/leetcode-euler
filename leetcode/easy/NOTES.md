## [88. Merge Sorted Array](https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

**Problem:**  
Merge two sorted integer arrays `nums1` and `nums2` into one sorted array in-place.  
- `nums1` has size `m + n` with first `m` elements valid.  
- `nums2` has size `n`.  
- Merge result should be in `nums1`.  

### Intuition  
- Start merging from the **end** of both arrays (avoid overwriting valid elements in `nums1`).  
- Use three pointers:  
  - `m - 1` → last valid element in `nums1`  
  - `n - 1` → last element in `nums2`  
  - `last` → last index in final merged array (`m + n - 1`)  
- Compare from the back and place the larger element at `nums1[last]`.  

### Complexity  
- **Time:** `O(m + n)` (iterate through both arrays once)  
- **Space:** `O(1)` (in-place merge)  

---
---

## [27. Remove Element](https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150)

**Problem:**  
Remove all instances of `val` in-place from array `nums` and return the new length `k`.

### Intuition  
- Use **two pointers**:  
  - `i` → iterate through the full array  
  - `k` → tracks the position of the next valid element  
- If `nums[i] != val`, copy it forward to `nums[k]`.  

### Complexity  
- **Time:** `O(n)` (single pass through array)  
- **Space:** `O(1)` (in-place, no extra array)  

---
