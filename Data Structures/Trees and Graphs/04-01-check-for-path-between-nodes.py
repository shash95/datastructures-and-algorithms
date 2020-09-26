########################################################################################################################
# Create graph from adjacency list and implement BFS and DFS. Assumption: Connected graph
########################################################################################################################
from collections import deque


class Graph:

    def __init__(self):
        self.node_list = []

    def add_to_graph(self, node):
        self.node_list.append(node)


class Node:

    def __init__(self, value):
        self.data = value
        self.visited = False
        self.outbound_edges = []


class ImplementGraph:

    def add_edge(self, graph, source_index, target_index, bidirectional=False):
        graph.node_list[source_index].outbound_edges.append(graph.node_list[target_index])
        if bidirectional:
            graph.node_list[target_index].outbound_edges.append(graph.node_list[source_index])

    # noinspection PyMethodMayBeStatic
    def create_graph(self, graph, node_list):
        source = None
        # current_node_list = []
        # adding nodes
        for node_value in node_list:
            new_node = Node(node_value)
            if source is None:
                source = new_node
            graph.add_to_graph(new_node)
            # current_node_list.append(new_node)

        # # adding edge information to each node
        # for node_value in adjacency_list.keys():
        #     for adjacent_node in adjacency_list[node_value]:
        #         current_node_list[node_value].outbound_edges.append(current_node_list[adjacent_node])

        return source

    # noinspection PyMethodMayBeStatic
    def print_graph_adjacency(self, graph):
        for node in graph.node_list:
            outbound_edge_list = []
            for adjacent_node in node.outbound_edges:
                outbound_edge_list.append(str(adjacent_node.data))
            print("Node : {}, adjacent nodes: ({})".format(str(node.data), str(','.join(outbound_edge_list))))

    # noinspection PyMethodMayBeStatic
    def reset_graph(self, graph):
        # method resets visited flag for all nodes
        for node in graph.node_list:
            node.visited = False

    # noinspection PyMethodMayBeStatic
    def check_path(self, source, target):
        q = deque()
        source.visited = True
        q.append(source)

        while len(q) != 0:
            current_node = q.popleft()
            for node in current_node.outbound_edges:
                if node == target:
                    return True
                if not node.visited:
                    q.append(node)

        return False


if __name__ == '__main__':
    # adjacency_list = {
    #     0: [2,6],
    #     1: [4],
    #     2: [3],
    #     3: [5],
    #     4: [],
    #     5: [6],
    #     6: [1]
    # }
    # defining nodes and creating the graph
    node_list = [0, 1, 2, 3, 4, 5, 6]
    g = Graph()
    ImplementGraph().create_graph(g, node_list)

    # adding edges
    ImplementGraph().add_edge(g, 0, 2)
    ImplementGraph().add_edge(g, 0, 6)
    ImplementGraph().add_edge(g, 1, 4)
    # ImplementGraph().add_edge(g, 2, 3)
    ImplementGraph().add_edge(g, 3, 5)
    ImplementGraph().add_edge(g, 5, 6)
    ImplementGraph().add_edge(g, 6, 1)
    ImplementGraph().add_edge(g, 4, 5)

    ImplementGraph().print_graph_adjacency(g)

    path_exists = ImplementGraph().check_path(g.node_list[0], g.node_list[5])
    print(path_exists)