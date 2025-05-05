from src.solvers.base import MinimumSpanningTreeBaseSolver
from src.data_manager.data_loader import DataLoader
from src.entities.edges import Edge
from src.entities.data_structures import UnionFind


INFINITY = 1000000


class BoruvkaMstSolver(MinimumSpanningTreeBaseSolver):
    def __init__(self, config):
        super().__init__(config)

    def add_undirected_edges(self):
        edges_raw = DataLoader(self.config).load_edges_data()
        for edge_raw in edges_raw:
            self.add_edge(edge_raw[0], edge_raw[1], edge_raw[2])

    def solve(self):
        if self.solved:
            return
        self.solved = True

        edge_count = 0
        completed = False

        union_find = UnionFind(size=self.n)

        while not completed:
            # Initialize empty list of cheapest edges of all components
            union_find.initialize_component_cheapest_edge()

            for node in self.graph:
                for edge in self.graph[node]:
                    edge_start = edge.start
                    edge_end = edge.end
                    # Check only edges that connect different components
                    if not union_find.connected(edge_start, edge_end):
                        # Assign edge as cheapest for any of two components
                        self.check_if_cheapest(union_find, edge, edge_start)
                        self.check_if_cheapest(union_find, edge, edge_end)

            if union_find.if_component_cheapest_edge_empty():
                completed = True
            else:
                for edge in union_find.component_cheapest_edge.values():
                    if edge:
                        union_find.unify(edge.start, edge.end)
                        if edge not in self.mst_edges.values():
                            edge_count += 1
                            self.mst_edges[edge_count] = edge
                            self.mst_min_cost += edge.cost

        if edge_count == self.m:
            self.mst_exists = True

    def check_if_cheapest(self, union_find: UnionFind, edge: Edge, node: int):
        component_id = union_find.find(node)
        if (
                not union_find.component_cheapest_edge.get(component_id)
                or union_find.component_cheapest_edge[component_id].cost > edge.cost
        ):
            union_find.component_cheapest_edge[component_id] = edge
        # TODO: Add tie-breaking rule (equal costs) if needed for edge cases
