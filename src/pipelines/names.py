from enum import Enum


class MSTSolver(Enum):
    prim = "PrimMstSolver"
    kruskal = "KruskalMstSolver"
    boruvka = "BoruvkaMstSolver"
    reverse_delete = "ReverseDeleteMstSolver"
