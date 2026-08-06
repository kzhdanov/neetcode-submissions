import operator

class Solution:
    ops = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a / b)
    }

    def evalRPN(self, tokens: List[str]) -> int:
        stake = [int(tokens[0])]
        i = 1

        while i < len(tokens):
            arg = tokens[i]
            is_operator = tokens[i] in self.ops
            if is_operator:
                next_val = stake.pop()
                prev_val = stake.pop()
                stake.append(int(self.ops[tokens[i]](prev_val, next_val)))
            else:
                stake.append(int(tokens[i]))

            i += 1

        return stake[0]   