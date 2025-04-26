from abc import abstractmethod
from collections import defaultdict

from src.config.config import Config
from src.data_manager.data_loader import DataLoader
from src.entities.edges import Edge


class MinimumSpanningTreeBaseSolver:
    number_of_edges = None
    solved = False
    mst_exists = False
    graph = defaultdict(list)
    # Outputs
    mst_min_cost = 0
    mst_edges = defaultdict(list)

    def __init__(self, config: Config):
        self.n = config.node_count
        self.s = config.source_id
        self.t = config.sink_id
        self.config = config

        self.m = self.n - 1  # number of edges in MST
        self.visited = self.n * [False]

    @abstractmethod
    def solve(self):
        pass

    def add_directed_edges(self):
        edges_raw = DataLoader(self.config).load_edges_data()
        for edge_raw in edges_raw:
            self.add_edge(edge_raw[0], edge_raw[1], edge_raw[2])

    def add_undirected_edges(self):
        edges_raw = DataLoader(self.config).load_edges_data()
        for edge_raw in edges_raw:
            self.add_edge(edge_raw[0], edge_raw[1], edge_raw[2])
            self.add_edge(edge_raw[1], edge_raw[0], edge_raw[2])

    def add_edge(self, start_node, end_node, cost):
        edge1 = Edge(start_node, end_node, cost)

        self.graph[start_node].append(edge1)

    def get_mst(self):
        self.solve()
        if self.mst_exists:
            return self.mst_edges
        else:
            return None

    def get_mst_cost(self):
        self.solve()
        if self.mst_exists:
            return self.mst_min_cost
        else:
            return None

    def if_mst_exists(self):
        self.solve()
        return self.mst_exists
