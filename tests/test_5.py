from graph import GraphGroup, ExceptSymbol
from graph.testing import debug_routes, debug_symbols
from graph.parser import process_symbol

if __name__ == '__main__':
    group = GraphGroup()

    all_symbol = ExceptSymbol()

    group.insert("A",
                 keys=[all_symbol],
                 init_graph=True,
                 exit_graph=True
                 )

    group.insert("B",
                 keys=[all_symbol]
                 )

    group.insert("C",
                 keys=['a'],
                 recursive_keys=[all_symbol, 'a']
                 )

    all_symbol.insert('a')

    group["A"].insert(group["B"])
    group["B"].insert(group["A"])

    group["A"].insert(group["C"])
    group["B"].insert(group["C"])

    print("All symbols: " + str(group.all_symbols))

    symbols = [
        "a",
        "aaaaa",
        "a*************a",
        "***************a"
        "xyz",
        "xxxxyz",
        "yz",
        "x",
        "xxxxxx",
    ]

    for symbol, routes, is_valid in debug_routes(group.root, symbols):
        print(f"'{symbol}' " + ("is valid" if is_valid else "is invalid"))

        for r in routes:
            print(f"{r[0]} -> {r[1]}")
