class DataLoader:
    def __init__(self, config):
        self.file_path = config.input_file_path

    def load_edges_data(self):
        with open(self.file_path) as file:
            f = file.readlines()
        output = [[int(y) for y in x[:-1].split(" ")] for x in f]
        return output
