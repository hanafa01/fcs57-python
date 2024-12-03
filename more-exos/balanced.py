
def isBalanced(stri):
    open = []

    for x in stri:
        if x == '(':
            open.append(x)
        elif x == ')':
            if len(open) == 0:
                return False
            else:
                open.pop()

    return len(open) == 0

print(isBalanced('((()()))'))