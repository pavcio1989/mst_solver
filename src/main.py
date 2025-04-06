import sys
import logging
# Add content root to your path
sys.path.append('C:/Users/pawel/Desktop/Learning/mst_solver')

if __name__ == "__main__":
    from src.config.config import Config
    from src.loggers.mst_logger import MSTLogger
    from src.pipelines.pipeline import Pipeline

    logger = MSTLogger(__name__, level=logging.INFO)

    config = Config()

    pipeline = Pipeline(config)

    pipeline.run()
