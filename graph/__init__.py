from typing import Union, Iterable, Any, List


class Symbol:
    def __init__(self, except_symbols: Union[List[str], None] = None):
        self.__except_symbols = {*except_symbols} if except_symbols else []

    @property
    def except_symbols(self) -> List[str]:
        return list(self.__except_symbols)

    def insert(self, symbol: str) -> None:
        self.__except_symbols.append(symbol)

    def __eq__(self, other: Union[str, Any]) -> bool:
        return other in self.except_symbols


class ExceptSymbol(Symbol):
    def __init__(self, *args):
        super(ExceptSymbol, self).__init__(*args)

    def __eq__(self, other: Union[str, Any]) -> bool:
        return other not in self.except_symbols


class AllSymbol(Symbol):
    def __init__(self, *args):
        super(AllSymbol, self).__init__(*args)

    def __eq__(self, other: Union[str, Any]) -> bool:
        return True


FLAG_RECURSIVE_KEYS = "recursive_keys"
FLAG_INIT_GRAPH = "init_graph"
FLAG_EXIT_GRAPH = "exit_graph"
FLAG_NAME = "name"


class GraphNode:
    def __init__(self, keys: Union[List[str], None] = None, childs: Union[List[str], None] = None, **kwargs):
        self.__symbols = [*keys] if not keys is None else []
        self.__graph_nodes = [*childs] if not childs is None else []
        self.__is_recursive = FLAG_RECURSIVE_KEYS in kwargs
        self.__recursive_keys = [] if not self.is_recursive else list(kwargs[FLAG_RECURSIVE_KEYS])
        self.__init = kwargs[FLAG_INIT_GRAPH] if FLAG_INIT_GRAPH in kwargs else False
        self.__exit = kwargs[FLAG_EXIT_GRAPH] if FLAG_EXIT_GRAPH in kwargs else False
        self.__name = kwargs[FLAG_NAME] if FLAG_NAME in kwargs else None

    @property
    def name(self) -> Union[str, None]:
        return self.__name

    @property
    def is_exit(self) -> bool:
        return self.__exit

    @property
    def is_init(self) -> bool:
        return self.__init

    @property
    def is_end(self) -> bool:
        return len(self.__graph_nodes) == 0

    @property
    def is_recursive(self) -> bool:
        return self.__is_recursive

    @property
    def recursive_symbols(self) -> List[str]:
        return self.__recursive_keys

    @property
    def symbols(self) -> List[str]:
        return self.__symbols

    @property
    def graph_nodes(self) -> List[Any]:
        return self.__graph_nodes

    def insert(self, c) -> None:
        self.__graph_nodes.append(c)

    def __iter__(self) -> Iterable:
        return iter(self.__graph_nodes)

    def __getitem__(self, item: int) -> Any:
        return self.graph_nodes[item]

    def __gt__(self, other: Union[str, Any]) -> bool:
        return self.name == other if isinstance(other, str) else self.name == other.name

    def __ge__(self, other: Union[str, Any]) -> bool:
        return self.name > other if isinstance(other, str) else self.name > other.name


class GraphGroup:
    def __init__(self):
        self.__all_symbols = set()
        self.__graph_root = None
        self.__graphs_nodes = {}

    @property
    def all_symbols(self) -> List[str]:
        return list(self.__all_symbols)

    @property
    def graphs_nodes(self) -> List[GraphNode]:
        return [g for _, g in self.__graphs_nodes.items()]

    @property
    def graphs_names(self) -> List[str]:
        return [n for n, _ in self.__graphs_nodes.items()]

    @property
    def root(self) -> Union[GraphNode, None]:
        return self.__graph_root

    def __contains__(self, name: str) -> bool:
        return name in self.graphs_names

    def __getitem__(self, name: str) -> Union[GraphNode, None]:
        if name in self:
            return self.__graphs_nodes[name]

        raise KeyError(f"graph {name} no found")

    def insert(self, name: str, **kwargs) -> None:
        flag_init_graph = kwargs[FLAG_INIT_GRAPH] if FLAG_INIT_GRAPH in kwargs else False

        if name in self:
            raise ValueError("GraphNode is included")
        else:
            graph = GraphNode(name=name, **kwargs)

            [self.__all_symbols.add(s) for s in graph.symbols if isinstance(s, str)]

            if flag_init_graph:
                self.__graph_root = graph

            self.__graphs_nodes[name] = graph
