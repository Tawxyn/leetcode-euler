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

# [383. Ransom Note](https://leetcode.com/problems/ransom-note/?envType=study-plan-v2&envId=top-interview-150)

**Problem:**  
Given two strings `ransomNote` and `magazine`, return `True` if `ransomNote` can be constructed by using the letters from `magazine`. Each letter in `magazine` can only be used once.  

### Intuition  
- First, if `ransomNote` is longer than `magazine`, it’s impossible → return `False`.  
- Use a **frequency counter** (dictionary) to track available characters in `magazine`.  
- Loop through `ransomNote`:  
  - If character not available in counter → return `False`.  
  - If available but only one left → remove it from counter.  
  - Otherwise → decrement its count.  
- If all characters matched, return `True`.  

### Complexity  
- **Time:** `O(m + n)` (iterate once over `magazine` and once over `ransomNote`)  
- **Space:** `O(k)` (at most 26 letters in dictionary, so effectively `O(1)`)  

---
---

# [205. Isomorphic Strings](https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150)

**Problem:**  
Given two strings `s` and `t`, return `True` if they are *isomorphic*.  
Two strings are isomorphic if the characters in `s` can be replaced to get `t`, with each character mapping one-to-one (no two characters map to the same character).

### Intuition  
- Need to check if characters in `s` map consistently to characters in `t`, and vice versa.  
- Use **two hash maps**:  
  - `mapST` → maps characters from `s` to `t`.  
  - `mapTS` → maps characters from `t` to `s`.  
- While iterating:  
  - If a mapping exists but doesn’t match, return `False`.  
  - Otherwise, update the mapping.  
- If no conflicts are found, return `True`.

### Complexity  
- **Time:** `O(n)` (single pass through both strings of length `n`)  
- **Space:** `O(k)` (at most all unique characters stored in maps, bounded by alphabet size)  

---
---
