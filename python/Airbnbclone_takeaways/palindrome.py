def palindrome(s: str) -> bool:    #def palindrome(s)
    s = s.lower()
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

print(palindrome("radaR"))
print(palindrome("radaj"))