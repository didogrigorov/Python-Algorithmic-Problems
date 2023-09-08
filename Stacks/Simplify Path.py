def simplifyPath(path: str) -> str:
    stack = []
    current = ""

    for c in path:
        if c == "/":
            if current == "..":
                if stack: stack.pop()
            elif current != "" and current != ".":
                stack.append(current)
            current = ""
        else:
            current += c

    return "/" + "/".join(stack)

path = "/a//b////c/d//././/.."
print(simplifyPath(path))