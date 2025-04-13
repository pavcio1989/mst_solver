class Edge:
    flow: float = 0
    residual = None

    def __init__(self, start, end, cost):
        self.start = start
        self.end = end
        self.cost = cost

    def compare_to(self, other):
        return self.cost - other.cost

    def __str__(self):
        return f"Edge {self.start} -> {self.end} | cost = {self.cost}"
