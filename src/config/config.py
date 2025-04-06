import yaml


class Config:
    def __init__(self):
        self.input = None

        # Data YAML
        with open('src/config/data.yml', 'r') as data_file:
            self.input = yaml.safe_load(data_file)

        self.input_file_path = self.input['data']['input_file']

        self.node_count = self.input['data']['input_file_details']['node_count']
        self.source_id_raw = self.input['data']['input_file_details']['source_id']
        self.sink_id_raw = self.input['data']['input_file_details']['sink_id']

        # Set source and sink index
        self.source_id = self.node_count - 2
        self.sink_id = self.node_count - 1

        self.output_data_folder = self.input['data']['output_data_folder']
        self.output_image_folder = self.input['data']['output_image_folder']

        # Pipeline YAML
        with open('src/config/pipeline.yml', 'r') as pipeline_file:
            self.input = yaml.safe_load(pipeline_file)

        self.solvers = {}
        for solver_name in self.input['solvers']:
            self.solvers[solver_name] = self.input['solvers'][solver_name]

        self.generate_report = self.input['report']
