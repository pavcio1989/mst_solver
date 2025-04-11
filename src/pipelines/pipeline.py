import logging

from src import solvers
from src.config.config import Config
from src.pipelines.names import MSTSolver
from src.utils.visuals import visualize_points_and_flows


logger = logging.getLogger('mst')


class Pipeline:
    def __init__(self, config: Config):
        self.solvers = config.solvers
        self._output_image_path = f"{config.output_image_folder}/{config.input_file_path.split('/')[-1].split('.')[-2]}_flow_chart.png"
        self.config = config

    def run(self):
        for solver_name in self.solvers:
            if self.solvers[solver_name]:
                logger.info(f"Minimum spanning tree solver: {solver_name} | In scope: YES")

                # Initialize MaxFlow solver class
                solver: solvers.MinimumSpanningTreeBaseSolver = \
                    getattr(solvers, MSTSolver[solver_name].value)(self.config)

                # Create graph
                solver.add_directed_edges()

                # Visualise network flow graph
                dg, pos = solver.get_directed_graph()

                visualize_points_and_flows(dg, pos, self._output_image_path)
            else:
                logger.info(f"Minimum spanning tree solver: {solver_name} | In scope: NO")
