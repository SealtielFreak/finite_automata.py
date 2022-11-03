from graph import GraphGroup
from graph.testing import debug_routes

if __name__ == '__main__':
    group = GraphGroup()

    group.insert("A",
                 keys='b', )

    group.insert("B",
                 keys='a',
                 init_graph=True,)

    group.insert("C",
                 keys='a',
                 exit_graph=True)

    group.insert("D",
                 keys='b',
                 recursive_keys=['b'])

    group.insert("E",
                 keys='b',
                 recursive_keys=['b', 'a'])

    group["A"].insert(group["B"])
    group["A"].insert(group["D"])

    group["B"].insert(group["A"])
    group["B"].insert(group["D"])
    group["B"].insert(group["C"])

    group["C"].insert(group["B"])
    group["C"].insert(group["E"])

    group["D"].insert(group["A"])
    group["D"].insert(group["B"])

    symbols = [
        "a",
        "aa"
        "ab",
        "ba",
        "bba",
        "bbaa",
        "abaaaaaaaaaaaaaabbbbababab",
        "bbbbbbbbbbbbbbbbbb"
    ]

    symbols += [*str(input("Enter symbols (separetes with a space): ")).split(" ")]

    for symbol, routes, is_valid in debug_routes(group.root, symbols):
        print(f"{symbol} " + ("is valid" if is_valid else "is invalid"))

        for r in routes:
            print(f"{r[0]} -> {r[1]}")
