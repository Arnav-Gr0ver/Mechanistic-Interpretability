#
# diff: med
# sol: space optimal :( not time
#   time complex | O(n^2 * m)
#   space complex | O(m)
#   time | 00:37:05.67
# 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #for each element determine if other elements are anagrams
        #if they are put into another list

        def isAnagram(str1, str2):
            hash_s1 = {}
            hash_s2 = {}
            for c in str1:
                if c not in hash_s1:
                    hash_s1[c] = 1
                else:
                    hash_s1[c] += 1
            for c in str2:
                if c not in hash_s2:
                    hash_s2[c] = 1
                else:
                    hash_s2[c] += 1
            if (hash_s1.keys() != hash_s2.keys()):
                return False
            for c in hash_s1:
                if hash_s1[c] != hash_s2[c]:
                    return False
            return True

        used = [False] * len(strs)
        out = []
        
        for i in range(len(strs)):
            if not used[i]:
                group = [strs[i]]
                used[i] = True
                for j in range(i+1, len(strs)):
                    if not used[j] and isAnagram(strs[i], strs[j]):
                        group.append(strs[j])
                        used[j] = True
                out.append(group)
        return out
                    
            