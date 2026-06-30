class Solution:
    def isValid(self, s: str) -> bool:
        valid = []
        close = []

        for c in s:
            if c in "(){}[]":
                valid.append(c)

        for i in range(len(valid)-1, -1, -1):
            if valid[i] in ")}]":
                # [old, new]
                close.append(valid[i])
            else:
                if len(close) == 0:
                    return False
                temp = close.pop()
                match valid[i]:
                    case "(":
                        if temp != ")":
                            return False
                    case "{":
                        if temp != "}":
                            return False
                    case "[":
                        if temp != "]":
                            return False

        if len(close) != 0:
            return False
        return True