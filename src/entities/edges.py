class Edge:
    flow: float = 0
    residual = None

    def __init__(self, start, end, capacity):
        self.start = start
        self.end = end
        self.capacity = capacity

    def __str__(self):
        return f"Edge {self.start} -> {self.end} | capacity = {self.capacity}"
