class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ''.join(ch for ch in s if ch.isalnum()).lower()
        if len(word) > 1:
            mid = len(word)//2
            #padding = -1 if len(s) % 2 else 0
            left = mid-1
            right = mid+1 if len(word) % 2 else mid
            if word[left] != word[right]:
                    return False 
            print(left)
            print(right)
            while left != 0 and right != len(word)-1:
                print(word[left])
                print(word[right])
                if word[left] != word[right]:
                    return False 
                left -= 1
                right += 1
        return True
            
        
        