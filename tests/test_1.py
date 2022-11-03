from graph import GraphNode
from graph.testing import debug_symbols

if __name__ == '__main__':
    graph_a, graph_b = [
        GraphNode(
            keys='a',
            exit_graph=True,
            recursive_keys=['b']),
        GraphNode(
            keys='a',
            recursive_keys=['b']
        )
    ]

    graph_a.insert(graph_b)
    graph_b.insert(graph_a)

    input_str = [
        "aa",
        "aba",
        "abaa"
    ]

    root = graph_a

    [print(f"{s} " + ("is valid" if is_valid else "is invalid")) for s, is_valid in debug_symbols(root, input_str)]
