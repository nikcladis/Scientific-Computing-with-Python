ERR_SIZE = "Error: Too many problems."
ERR_OP = "Error: Operator must be '+' or '-'."
ERR_NUM = "Error: Numbers must only contain digits."
ERR_LEN = "Error: Numbers cannot be more than four digits."


def arithmetic_arranger(problems, display=False):
    if len(problems) > 5:
        return ERR_SIZE

    slicing_of_list = ' '.join(problems).split()

    a = []
    b = []
    op = []
    formatting = []

    for i in range(0, len(slicing_of_list), 3):
        a.append(slicing_of_list[i])
        op.append(slicing_of_list[i + 1])
        b.append(slicing_of_list[i + 2])

    for i in range(len(problems)):

        if op[i] != '+' and op[i] != '-':
            return ERR_OP

        try:
            if abs(int(a[i])) > 9999 or abs(int(b[i])) > 9999:
                return ERR_LEN
        except Exception:
            return ERR_NUM

        formatting.append(frmt(a[i], op[i], b[i], display))

    lines = formatting[0]
    space = " " * 4

    for x in formatting[1:]:
        for i in range(0, len(lines)):
            lines[i] += space + x[i]

    if not display:
        lines = lines[0:3]

    return '\n'.join(lines)


def frmt(a, op, b, display):
    x = int(a)
    y = int(b)
    calc = x + y if op == '+' else x - y
    base = calc if calc > 0 else 0 - calc
    n = max([len(a), len(b), len(str(base))]) if display else max([len(a), len(b)])

    calc = str(calc)
    n += 2
    result = [a.rjust(n), op + " " + b.rjust(n - 2), '-' * n]
    if display:
        result.append(calc.rjust(n))

    return result
