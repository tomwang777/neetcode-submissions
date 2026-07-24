class Solution:
    def isPalindrome(self, s: str) -> bool:
      clean_chars = [char.lower() for char in s if char.isalnum()]  
      clean_s = "".join(clean_chars)

      return clean_s == clean_s[::-1]