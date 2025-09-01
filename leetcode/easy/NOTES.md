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
