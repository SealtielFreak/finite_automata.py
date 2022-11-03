from graph import GraphNode
from graph.testing import debug_symbols

if __name__ == '__main__':
    graph_a, graph_b, graph_c = [
        GraphNode(
            keys=['a'],
            recursive_keys=['b', 'c'],
            exit_graph=True),
        GraphNode(
            keys=['a'],
            recursive_keys=['b']
        ),
        GraphNode(
            keys=['c'],
            recursive_keys=['a', 'b', 'c']
        )
    ]

    graph_a.insert(graph_b)
    graph_b.insert(graph_a)

    graph_b.insert(graph_c)

    input_str = [
        "aa"
        "ac",
        "aabaaacaaaa",
        "aabacbbb",
        "ba",
        "ab",
        "aacccccc",
        "bcz"
    ]

    root = graph_a

    [print(f"{s} " + ("is valid" if is_valid else "is invalid")) for s, is_valid in debug_symbols(root, input_str)]
