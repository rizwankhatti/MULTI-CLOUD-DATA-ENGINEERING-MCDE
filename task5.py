# Task 05 - Calculator (no eval)
# Think: brackets first, then * and /, then + and -
tokens = []
pos = 0

def expression():                        # + and -
    global pos
    value = term()
    while pos < len(tokens) and tokens[pos] in "+-":
        op = tokens[pos]
        pos += 1
        value = value + term() if op == "+" else value - term()
    return value

def term():                              # * and /
    global pos
    value = factor()
    while pos < len(tokens) and tokens[pos] in "*/":
        op = tokens[pos]
        pos += 1
        right = factor()
        if op == "*":
            value = value * right
        elif right == 0:
            raise ZeroDivisionError("Divide by zero")
        else:
            value = value / right
    return value

def factor():                            # number, (brackets), or minus sign
    global pos
    if pos >= len(tokens):
        raise ValueError("Bad expression")
    t = tokens[pos]
    pos += 1
    if t == "-":
        return -factor()
    if t == "(":
        value = expression()
        if pos >= len(tokens) or tokens[pos] != ")":
            raise ValueError("Missing )")
        pos += 1
        return value
    if t.isdigit():
        return int(t)
    raise ValueError("Bad token " + t)

def calculate(text):
    global tokens, pos
    tokens = []
    number = ""
    for ch in text + " ":                # extra space flushes the last number
        if ch.isdigit():
            number += ch
        else:
            if number:
                tokens.append(number)
                number = ""
            if ch != " ":
                tokens.append(ch)
    pos = 0
    result = expression()
    if pos != len(tokens):
        raise ValueError("Bad expression")
    return float(result)

print(calculate("-(3 + 2) * 4 + 18 / 3"))    # -14.0
for bad in ["2 +", "(1 + 2", "5 / 0"]:
    try:
        calculate(bad)
    except (ValueError, ZeroDivisionError) as e:
        print(bad, "->", e)
