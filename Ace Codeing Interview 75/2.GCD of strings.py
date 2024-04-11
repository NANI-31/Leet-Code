"""
1071. Greatest Common Divisor of Strings
For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 
Example 1:
    Input: str1 = "ABCABC", str2 = "ABC"
    Output: "ABC"

Example 2:
    Input: str1 = "ABABAB", str2 = "ABAB"
    Output: "AB"

Example 3:
    Input: str1 = "LEET", str2 = "CODE"
    Output: ""
 

Constraints:
    1 <= str1.length, str2.length <= 1000
    str1 and str2 consist of English uppercase letters
"""

def gcdOfStrings(str1: str, str2: str) -> str:
    len1, len2 = len(str1), len(str2)
    gcd_len = ""
    a,b = len1,len2
    while b:
        a, b = b, a % b
        gcd_len = a
    divisor = str1[:gcd_len]
    
    if str1 == divisor * (len1 // gcd_len) and str2 == divisor * (len2 // gcd_len):
        return divisor
    else:
        return ""