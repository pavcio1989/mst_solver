# Minimum Spanning Tree solver overview

This Python repository allows to solve minimum spanning tree problem for any given graph (if a solution exists).

### Setup environment

Create a Python 3.12 venv, list of dependencies can be found in _./requirements.txt_ file.

### Run module

1. Prepare network flow data in as TXT file and put it in _./data/input/_ folder.

    File should be constructed in a way where each row corresponds to one directed edge of a graph, with a following
    row structure:

       <START_NODE_ID> <END_NODE_ID> <FLOW_VALUE>

    Example files can be found in /data/input/ folder.
2. Update the config file _./src/config/data.yml_ with information about the input data file.
    Config sections to be updated:

    - input_file, i.e. relative path to input file
    - input_file_details, i.e. number of nodes, id of source node, id of sink node

3. Run the maximum flow solver by executing the command:
        
        make run