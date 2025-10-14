from src.solvers.base import MinimumSpanningTreeBaseSolver
from src.data_manager.data_loader import DataLoader
from src.entities.edges import Edge
from src.entities.data_structures import UnionFind


class ReverseDeleteMstSolver(MinimumSpanningTreeBaseSolver):
    edge_list_sorted = []
    visited = None

    def __init__(self, config):
        super().__init__(config)
        visited = self.n * [0]

    def add_undirected_edges(self):
        edges_raw = DataLoader(self.config).load_edges_data()
        for edge_raw in edges_raw:
            self.add_edge(edge_raw[0], edge_raw[1], edge_raw[2])
            self.add_edge(edge_raw[1], edge_raw[0], edge_raw[2])

        # Sort list of edges by cost in descending order
        self.edge_list_sorted.sort(key=lambda x: x.cost, reverse=True)

    def add_edge(self, start_node, end_node, cost):
        edge1 = Edge(start_node, end_node, cost)

        self.graph[start_node].append(edge1)

        # Add edge to the sorted list for solver (only one edge version)
        if start_node < end_node:
            self.edge_list_sorted.append(edge1)

    def solve(self):
        if self.solved:
            return
        self.solved = True

        # Set initial MST edges as entire graph
        edge_count = len(self.edge_list_sorted)
        mst = self.graph.copy()

        # If initial set of edges does not span across all nodes, there cannot be any MST
        if edge_count < self.m:
            return

        for edge in self.edge_list_sorted:

            # Clear list of visited nodes
            self.visited = self.n * [0]

            # Run DFS algorithm to check if all nodes are still connected, starting with first node
            self.dfs(node=0, edge=edge, graph=mst)

            if all(self.visited):
                edge_count -= 1
                mst[edge.start].remove(edge)
            else:
                continue

        ################

        if edge_count == self.m:
            self.mst_exists = True

            # Store final MST parameters
            i = 0
            print(f"Final MST: {mst}")
            for _node in mst:
                for _edge in mst[_node]:
                    self.mst_edges[i] = _edge
                    self.mst_min_cost += _edge.cost
                    i += 1

    def visit(self, node):
        self.visited[node] = 1

    def is_visited(self, node):
        return self.visited[node] == 1

    def dfs(self, node, edge, graph):

        # Mark the current node as visited
        self.visit(node)

        for _edge in graph[node]:
            # Skip the edge that is a candidate (and its reverse) to be removed from current MST graph
            if _edge == edge:
                continue
            if _edge == edge.reverse():
                continue

            elif not self.is_visited(_edge.end):
                self.dfs(_edge.end, edge, graph)
        return
