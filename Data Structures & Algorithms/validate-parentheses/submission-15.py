class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if c in ")}]":
                if stack:
                    temp = stack.pop()
                    match temp:
                        case "(":
                            if c != ")":
                                return False
                        case "{":
                            if c != "}":
                                return False
                        case "[":
                            if c != "]":
                                return False
                else:
                    return False
            else:
                if c in "({[":
                    stack.append(c)

        return False if stack else True