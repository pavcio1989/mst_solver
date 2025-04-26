from src.solvers.base import MinimumSpanningTreeBaseSolver
from src.entities.data_structures import IndexedMinPQ


class PrimMstSolver(MinimumSpanningTreeBaseSolver):
    def __init__(self, config):
        super().__init__(config)

    def solve(self):
        if self.solved:
            return
        self.solved = True

        edge_count = 0

        ipq = IndexedMinPQ(self.n)

        self.relax_edges_at_node(ipq, self.s)

        while not ipq.is_empty() and edge_count != self.m:
            # Extract the next best (node, edge) pair from IPQ
            destination_node_index, _, edge = ipq.delete_min()

            edge_count += 1
            self.mst_edges[edge_count] = edge
            self.mst_min_cost += edge.cost

            self.relax_edges_at_node(ipq, destination_node_index)

        if edge_count == self.m:
            self.mst_exists = True

    def relax_edges_at_node(self, index_priority_queue: IndexedMinPQ, current_node_index):
        self.visited[current_node_index] = True

        edges = self.graph.get(current_node_index)

        for edge in edges:
            edge_end_index = edge.end
            # Skip edges pointing to already visited nodes
            if self.visited[edge_end_index]:
                continue
            if not index_priority_queue.contains(edge_end_index):
                # Insert edge for the first time
                index_priority_queue.insert(edge_end_index, edge, edge.cost)
            else:
                # Try to improve the cheapest edge at edge_end_node with the current edge in the IPQ
                index_priority_queue.decrease_key(edge_end_index, edge, edge.cost)
