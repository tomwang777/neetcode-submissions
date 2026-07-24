class Solution:
    def isPalindrome(self, s: str) -> bool:
      clean_chars = [char.lower() for char in s if char.isalnum()]  
      clean_s = "".join(clean_chars)
      n = len(clean_s)
      left = 0
      right = n - 1
      while left < right:
            if clean_s[left] != clean_s[right]:
                return False
            else:
                left += 1
                right -= 1
      return True
