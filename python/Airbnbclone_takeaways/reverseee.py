strng = ["h","e","l","l","o"]
newstring = strng[::-1]

print(newstring)

# alternative, that modifies the the list in place it does not return a new list, just do this
"""
def reverseString(s):
s.reverse()
"""


"""
In C#
public class Solution {
    public void ReverseString(char[] s) {
        int left = 0;
        int right = s.Length - 1;
        
        while (left < right) 
        {
            var temp = s[left];
            s[left] = s[right];
            s[right] = temp;
            
            left++;
            right--;
        }
            
        
    }
}

public class Solution {
    public void ReverseString(char[] s) {
        Array.Reverse(s);
    }
}
"""