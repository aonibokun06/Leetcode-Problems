# Given two strings needle and haystack, 
# return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):   #Edge Case
            return -1
            
        n = len(needle)
        for i in range(len(haystack)):
            if needle == haystack[i:n+i]: #Returns index if haystack substring equals needle
                return i
        return -1 