from collections import deque

from src.solvers.base import MinimumSpanningTreeBaseSolver


MAX_COST = 1000000

class PrimMstSolver(MinimumSpanningTreeBaseSolver):
    def __init__(self, config):
        super().__init__(config)

    def solve(self):
        if self.solved:
            return
        self.solved = True

        m = self.n - 1
        edge_count = 0
        visited = []
        mst_edges = []

        ipq = deque()

    def relax_edges_at_node(self, current_node_index):
        self.visited[current_node_index] = True

        edges = self.graph.get(current_node_index)

        for edge in edges:
            dest_node_index = edge.end
            # Skip edges pointing to already visited nodes
            if self.visited[dest_node_index]:
                continue

