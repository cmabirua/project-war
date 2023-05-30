def isValid(s):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for c in s:
        if c in '({[':
            stack.append(c)
        elif c in ')}]':
            if not stack or stack[-1] != brackets[c]:
                return False
            stack.pop()
    
    return len(stack) == 0

print(isValid("()"))
print(isValid("()[]}"))
