#Easy
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:

# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.
# 3. Every close bracket has a corresponding open bracket of the same type

def isValid(self, s: str) -> bool:
        brackets = {"}" : "{", "]" : "[", ")" : "("}
        stack = []
        if len(s) %2 != 0:
            return False
        for char in s:
            size = 0
            if char in brackets:
                if not stack:
                    return False
                if brackets[char] != stack.pop():
                    return False
            else:
                stack.append(char)
        return not stack