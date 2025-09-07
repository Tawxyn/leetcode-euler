class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        
        if len(magazine) < len(ransomNote):
            return False

        counter = {}
        for c in magazine:
            counter[c] = counter.get(c, 0) + 1

        for c in ransomNote:
            if c not in counter:
                return False
            elif counter[c] == 1:
                del counter[c]
            else:
                counter[c] -= 1
        
        return True
