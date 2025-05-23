import logging
from collections import defaultdict

from src import solvers
from src.config.config import Config
from src.pipelines.names import MSTSolver
from src.utils.visuals import visualize_minimum_spanning_tree


logger = logging.getLogger('mst')


class Pipeline:
    def __init__(self, config: Config):
        self.solvers = config.solvers
        self._output_image_folder_path = f"{config.output_image_folder}/{config.input_file_path.split('/')[-1].split('.')[-2]}"
        self.config = config

    def run(self):
        for solver_name in self.solvers:
            if self.solvers[solver_name]:
                logger.info(f"Minimum spanning tree solver: {solver_name} | In scope: YES")

                # Initialize MaxFlow solver class
                solver: solvers.MinimumSpanningTreeBaseSolver = \
                    getattr(solvers, MSTSolver[solver_name].value)(self.config)

                # Create graph
                solver.add_undirected_edges()

                if solver.if_mst_exists():
                    logger.info(f"MST cost: {solver.get_mst_cost()}")
                    logger.info(f"MST edges: {solver.get_mst()}")
                    for edge in solver.get_mst().values():
                        print(edge)

                    # Visualise network flow graph
                    dg, pos = solver.get_directed_graph()
                    _output_image_file_path = self._output_image_folder_path+"_flow_chart_"+solver_name+".png"
                    visualize_minimum_spanning_tree(dg, pos, _output_image_file_path, solver.get_mst().values())

                else:
                    logger.info(f"Minimum spanning tree solver: {solver_name} | No MST exists.")
                    for edge in solver.mst_edges.values():
                        print(edge)

            else:
                logger.info(f"Minimum spanning tree solver: {solver_name} | In scope: NO")
