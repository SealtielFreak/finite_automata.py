from graph import GraphGroup, ExceptSymbol, AllSymbol
from graph.testing import debug_routes
from graph.parser import process_symbol


if __name__ == '__main__':
    group = GraphGroup()

    all_symbol = AllSymbol()
    except_symbol = ExceptSymbol(
        list("/*")
    )

    group.insert("A",
                 keys='/',
                 recursive_keys=[except_symbol],
                 init_graph=True,
                 exit_graph=True)

    group.insert("B",
                 keys='/',)

    group.insert("C",
                 keys='*',
                 recursive_keys=[except_symbol])

    group.insert("D",
                 keys='*',
                 recursive_keys=[])

    group.insert("E",
                 keys=[except_symbol],
                 recursive_keys=[all_symbol])

    group["A"].insert(group["B"])

    group["B"].insert(group["C"])

    group["C"].insert(group["D"])

    group["D"].insert(group["A"])

    group["B"].insert(group["E"])
    group["C"].insert(group["E"])
    group["D"].insert(group["E"])

    print("All symbols: " + str(group.all_symbols))

    symbols = [
        "/**/",
        "/*this is a comment*/",
        "/* bad comment",
        "/*firts comment*/ /*second comment*/",

        """
        #include <stdio.h>
        /*
            Hello world in C
        */
        
        int main() {
            printf("%s\n", "Hello world");
        }
        """
    ]

    for symbol, routes, is_valid in debug_routes(group.root, symbols):
        n_line = '\n'
        print(f"'{str().join(symbol.split(n_line))}' " + ("is valid" if is_valid else "is invalid"))

        for r in routes:
            print(f"{r[0]} -> {r[1]}")
