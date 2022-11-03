class Symbol:
    pass


def process_symbol(expr: str):
    def separate_sub_symbols(sub_expr: str):
        length_symbols = len(sub_expr)
        sub_symbols = ""
        i = 0

        while i <= length_symbols:
            j = i + 1

            if j >= length_symbols:
                break

            if sub_expr[j] == '(':
                sub_symbols += sub_expr[i]

            if sub_expr[j] == ')':
                break

            sub_symbols += sub_expr[i]
            i += 1

    symbols = []
    length_symbols = len(expr)
    i = 0

    while i <= length_symbols:
        sym = expr[i]

        if sym in ['(']:
            separate_sub_symbols()

        if not sym in ['*', '+']:
            pass

        i += 1

    return symbols
