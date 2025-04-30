import plotly.graph_objects as go


NODE_SIZE = 20


def visualize_points_and_flows(graph, node_coordinates, output_path):
    """
    Function to visualize points and flows
    :param graph: Graph
    :param node_coordinates: Node coordinates
    :param output_path: Output path
    :return:
    """

    color_map = {"source": 'rgb(0, 128, 155)',
                 "middle": 'rgb(191, 2, 2)',
                 "sink": 'rgb(255, 128, 0)',
                 }

    fig = go.Figure()

    # Nodes
    fig.add_trace(
        go.Scatter(
            x=[float(node_coordinates[node][0]) for node in graph.nodes],
            y=[float(node_coordinates[node][1]) for node in graph.nodes],
            text=[f"{node[0]}_{node[1]['type']}" for node in graph.nodes.data()],
            mode='markers+text',
            textposition="top center",
            marker=dict(
                color=[color_map[node[1]["type"]] for node in graph.nodes.data()],
                size=NODE_SIZE,
                line=dict(
                    width=5,
                    color='rgba(68, 68, 68, 0)'
                ),
            )
        )
    )

    # Flows
    for edge in graph.edges.data():
        if not edge[2]["is_residual"]:
            # Introduce minimal opacity value for edges with no flow
            opacity_correction = 0.05 if edge[2]['flow'] / edge[2]['capacity'] < 1 else 0

            fig.add_trace(
                go.Scatter(
                    x=[node_coordinates[edge[0]][0], node_coordinates[edge[1]][0]],
                    y=[node_coordinates[edge[0]][1], node_coordinates[edge[1]][1]],
                    mode='lines+markers',
                    line=dict(
                        width=edge[2]["capacity"],
                        color='rgb(0, 128, 155)',
                    ),
                    marker=dict(
                        symbol="arrow-wide",
                        size=15,
                        angleref="previous",
                    ),
                    opacity=opacity_correction + edge[2]['flow'] / edge[2]['capacity'],
                )
            )

            fig.add_annotation(x=0.5 * (node_coordinates[edge[0]][0] + node_coordinates[edge[1]][0]),
                               y=0.5 * (node_coordinates[edge[0]][1] + node_coordinates[edge[1]][1]),
                               text=f"{edge[2]['flow']} / {edge[2]['capacity']}",
                               showarrow=False,
                               yshift=10)

    fig.update_layout(showlegend=False)

    fig.write_image(output_path)


def visualize_minimum_spanning_tree(graph, node_coordinates, output_path, mst_edges=None):
    """
    Function to visualize graph with minimum spanning tree
    :param graph: Graph
    :param node_coordinates: Node coordinates
    :param mst_edges:
    :param output_path: Output path
    :return:
    """

    color_map = {"source": 'rgb(0, 128, 155)',
                 "middle": 'rgb(191, 2, 2)',
                 "sink": 'rgb(255, 128, 0)',
                 }

    fig = go.Figure()

    # Nodes
    fig.add_trace(
        go.Scatter(
            x=[float(node_coordinates[node][0]) for node in graph.nodes],
            y=[float(node_coordinates[node][1]) for node in graph.nodes],
            mode='markers',
            marker=dict(
                color=[color_map[node[1]["type"]] for node in graph.nodes.data()],
                size=NODE_SIZE,
                line=dict(
                    width=5,
                    color='rgba(68, 68, 68, 0)'
                ),
            )
        )
    )

    # Edges - all
    for edge in graph.edges.data():

        opacity_base = 0.3
        width_base = 1

        fig.add_trace(
            go.Scatter(
                x=[node_coordinates[edge[0]][0], node_coordinates[edge[1]][0]],
                y=[node_coordinates[edge[0]][1], node_coordinates[edge[1]][1]],
                mode='lines',
                line=dict(
                    width=width_base,
                    color='rgb(0, 128, 155)',
                ),
                opacity=opacity_base
            )
        )

        fig.add_annotation(x=0.5 * (node_coordinates[edge[0]][0] + node_coordinates[edge[1]][0]),
                           y=0.5 * (node_coordinates[edge[0]][1] + node_coordinates[edge[1]][1]),
                           text=f"{edge[2]['cost']}",
                           showarrow=False,
                           yshift=10)

    # Edges - MST
    if mst_edges:
        for edge in mst_edges:

            opacity_mst = 1
            width_mst = 3

            fig.add_trace(
                go.Scatter(
                    x=[node_coordinates[edge.start][0], node_coordinates[edge.end][0]],
                    y=[node_coordinates[edge.start][1], node_coordinates[edge.end][1]],
                    mode='lines',
                    line=dict(
                        width=width_mst,
                        color='rgb(0, 128, 155)',
                    ),
                    opacity=opacity_mst
                )
            )

    fig.update_layout(showlegend=False)

    fig.write_image(output_path)
