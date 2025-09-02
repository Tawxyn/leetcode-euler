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
---

## [26. Remove Duplicates from Sorted Array](https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150)

**Problem:**  
Given a sorted array `nums`, remove the duplicates in-place such that each unique element appears only once. Return the new length `k`.  
- The relative order of elements should be kept the same.  
- Must use **O(1)** extra space.  

### Intuition  
- Since the array is sorted, duplicates will always be **adjacent**.  
- Use **two pointers**:  
  - `i` → scans through array  
  - `k` → tracks the position of the next unique element  
- Compare `nums[i]` with the **last unique element** (`nums[k-1]`).  
- If different, place it at `nums[k]` and move `k` forward.  

### Complexity  
- **Time:** `O(n)` (single pass)  
- **Space:** `O(1)` (in-place, no extra data structures)  

---
---

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

## [189. Rotate Array](https://leetcode.com/problems/rotate-array/description/?envType=study-plan-v2&envId=top-interview-150)

**Problem:**  
Given an integer array `nums`, rotate the array to the right by `k` steps, where `k` is non-negative.  

### Intuition  
- Rotating by `k` means the last `k` elements move to the front.  
- A neat trick: **use array reversal**.  
  1. Reverse the entire array.  
  2. Reverse the first `k` elements.  
  3. Reverse the remaining `n - k` elements.  
- This reorders the array correctly in-place.  

### Complexity  
- **Time:** `O(n)` (each reversal takes linear time, total still `O(n)`)  
- **Space:** `O(1)` (in-place swaps only)  

---
---
