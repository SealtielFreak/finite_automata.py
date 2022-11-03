from graph import GraphNode
from graph.testing import debug_symbols

if __name__ == '__main__':
    graph_a, graph_b, graph_c = [
        GraphNode(
            keys=['a', 'b'],
            exit_graph=True),
        GraphNode(
            keys=['b'],
        ),
        GraphNode(
            keys=['a', 'c'],
            recursive_keys=['a', 'c']
        )
    ]

    graph_a.insert(graph_b)
    graph_b.insert(graph_a)

    graph_a.insert(graph_c)
    graph_b.insert(graph_c)

    graph_c.insert(graph_a)

    input_str = [
        "aa",
        "aab",
        "aabac",
        "ba",
        "ab",
        "bcz"
    ]

    root = graph_a

    [print(f"{s} " + ("is valid" if is_valid else "is invalid")) for s, is_valid in debug_symbols(root, input_str)]
