from typing import Union, Callable, Iterable, Any

from graph import GraphNode


def filterindex(function: Callable[[Any], bool], iterable: Iterable):
    return ([i for i, v in enumerate(iterable) if function(v)] + [-1])[0]


def filtergraph(graph: GraphNode, key: str) -> int:
    return filterindex(lambda c: key in c.symbols, graph.graph_nodes)


def to_next(graph: GraphNode, symbol: str) -> Union[GraphNode, None]:
    if symbol in graph.recursive_symbols:
        return graph

    i = filtergraph(graph, symbol)

    if i >= 0:
        return graph.graph_nodes[i]

    raise ValueError(f"Invalid key '{symbol}' for graph[{graph.name}], key symbol no found")


"""
def to_next(graph: GraphNode, key) -> Union[GraphNode, None]:
    i = filterindex(lambda c: key in c.keys, graph.child_nodes)

    if i >= 0:
        return graph.child_nodes[i]
    else:
        if key in graph.keys:
            return graph
        elif key in graph.recursive_keys:
            return graph

    raise ValueError("Invalid key for this graph, key symbol no found")
"""
