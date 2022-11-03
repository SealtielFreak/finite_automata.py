from typing import List, Tuple, Optional, Any

from graph import GraphNode
from graph.manipulation import to_next


def debug_symbols(root: GraphNode, inputs_symbols: List[str]) -> List[Tuple[str, bool]]:
    result_syms = []

    for s in inputs_symbols:
        aux = root

        try:
            for c in list(s):
                aux = to_next(aux, c)
        except ValueError:
            result_syms.append((s, False))  # meh
        else:
            result_syms.append((s, aux.is_exit))

    return result_syms


def debug_routes(root: GraphNode, inputs_symbols: List[str]) -> List[
    Tuple[str, List[Tuple[Tuple[Optional[str], Optional[str]], Any]], bool]]:
    result_syms = []

    for s in inputs_symbols:
        routes = []
        aux = root

        try:
            for c in list(s):
                later = aux
                aux = to_next(aux, c)

                routes.append(((later.name, aux.name), c))

        except ValueError as e:
            print(e)
        else:
            result_syms.append((s, routes, aux.is_exit))

    return result_syms
