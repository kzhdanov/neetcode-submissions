import operator

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": lambda a, b: int(a / b)
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stake = [tokens[0]]
        i = 1

        while i < len(tokens):
            arg = tokens[i]

            if tokens[i] in ops:
                next_val = stake.pop()
                prev_val = stake.pop()
                stake.append(ops[tokens[i]](int(prev_val), int(next_val)))
            else:
                stake.append(tokens[i])

            i += 1

        return int(stake[0])   