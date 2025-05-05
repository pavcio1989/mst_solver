from src.solvers.base import MinimumSpanningTreeBaseSolver
from src.data_manager.data_loader import DataLoader
from src.entities.edges import Edge
from src.entities.data_structures import UnionFind


class KruskalMstSolver(MinimumSpanningTreeBaseSolver):
    edge_list_sorted = []

    def __init__(self, config):
        super().__init__(config)

    def add_undirected_edges(self):
        edges_raw = DataLoader(self.config).load_edges_data()
        for edge_raw in edges_raw:
            self.add_edge(edge_raw[0], edge_raw[1], edge_raw[2])

        # Sort list of edges by cost in ascending order
        self.edge_list_sorted.sort(key=lambda x: x.cost, reverse=False)

    def add_edge(self, start_node, end_node, cost):
        edge1 = Edge(start_node, end_node, cost)

        self.graph[start_node].append(edge1)
        self.edge_list_sorted.append(edge1)

    def solve(self):
        if self.solved:
            return
        self.solved = True

        edge_count = 0

        union_find = UnionFind(size=self.n)

        for edge in self.edge_list_sorted:
            edge_start = edge.start
            edge_end = edge.end

            if (
                    not self.visited[edge_start]
                    or not self.visited[edge_end]
                    or not union_find.connected(edge_start, edge_end)
            ):
                self.visited[edge_start] = True
                self.visited[edge_end] = True

                union_find.unify(edge_start, edge_end)

                edge_count += 1
                self.mst_edges[edge_count] = edge
                self.mst_min_cost += edge.cost

        if edge_count == self.m:
            self.mst_exists = True
