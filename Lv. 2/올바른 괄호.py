def solution(s):
    stack = []
    if s[0] == "(":
        for ss in s:
            if ss == "(":
                stack.append(ss)
            else:
                if len(stack) == 0:
                    return False
                stack.pop()
        if len(stack) == 0:
            return True
    return False