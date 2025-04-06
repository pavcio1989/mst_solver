from abc import abstractmethod
from collections import defaultdict

from src.config.config import Config
from src.data_manager.data_loader import DataLoader
from src.entities.edges import Edge


class MinimumSpanningTreeBaseSolver:
    solved = False
    graph = defaultdict(list)

    def __init__(self, config: Config):
        self.n = config.node_count
        self.s = config.source_id
        self.t = config.sink_id
        self.config = config

    @abstractmethod
    def solve(self):
        pass

    def add_edges(self):
        edges_raw = DataLoader(self.config).load_edges_data()
        for edge_raw in edges_raw:
            self.add_edge(edge_raw[0], edge_raw[1], edge_raw[2])

    def add_edge(self, start_node, end_node, capacity):
        if capacity <= 0:
            raise Exception("Forward edge capacity <=0")
        edge1 = Edge(start_node, end_node, capacity)

        self.graph[start_node].append(edge1)

    def get_mst_cost(self):
        pass
