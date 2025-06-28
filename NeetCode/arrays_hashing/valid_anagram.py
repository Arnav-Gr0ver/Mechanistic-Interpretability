#
# diff: ez
# sol: time optimal
#   time complex | O(n+m)
#   space complex | O(n+m)
#   time | 00:05:19.99
# 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #exact same # of chars, different order
        #use hashmap to keep count of frequency, compare frequencies

        #count freq of chars in s
        hash_s = {}
        for c in s:
            if c not in hash_s:
                hash_s[c] = 1
            else:
                hash_s[c] += 1
        
        #count freq of chars in t
        hash_t = {}
        for c in t:
            if c not in hash_t:
                hash_t[c] = 1
            else:
                hash_t[c] += 1

        #comparison
        #same chars might not exist
        if hash_s.keys() != hash_t.keys():
            return False
        
        #char count migth not be equal
        for c in hash_s:
            if hash_s[c] != hash_t[c]:
                return False
    
        return True