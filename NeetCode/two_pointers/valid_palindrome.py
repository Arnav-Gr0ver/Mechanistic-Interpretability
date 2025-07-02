#
# diff: ez
# sol: almost there, operate on original string to get O(1) space
#   time complex | O(n)
#   space complex | O(n)
#   time | 00:07:50.88
# 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def preprocess(string):
            new = ""
            for c in s:
                if c.isalnum():
                    if c.isalpha():
                        new += c.lower()
                    else:
                        new += c
            return new
        processed_string = preprocess(s)
        print(processed_string)

        front_pointer = 0
        back_pointer = -1
        
        if len(processed_string) % 2 == 0:
            counter = len(processed_string) / 2
        else:
            counter = len(processed_string) / 2 + 0.5
        
        for i in range(int(counter)):
            if processed_string[front_pointer] != processed_string[back_pointer]:
                return False
            else:
                front_pointer += 1
                back_pointer -= 1
        
        return True