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

    # noinspection PyMethodMayBeStatic
    def create_graph(self, graph, adjacency_list):
        source = None
        current_node_list = []
        # adding nodes
        for node_value in adjacency_list:
            new_node = Node(node_value)
            if source is None:
                source = new_node
            graph.add_to_graph(new_node)
            current_node_list.append(new_node)

        # adding edge information to each node
        for node_value in adjacency_list.keys():
            for adjacent_node in adjacency_list[node_value]:
                current_node_list[node_value].outbound_edges.append(current_node_list[adjacent_node])

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
    def implement_dfs(self, source):
        # iterate on all outbound edges and visit if they are unvisited
        print(source.data)
        source.visited = True
        for node in source.outbound_edges:
            if not node.visited:
                self.implement_dfs(node)

    # noinspection PyMethodMayBeStatic
    def implement_bfs(self, source):
        q = deque()
        q.append(source)
        source.visited = True

        while len(q) != 0:
            current_node = q.popleft()
            print(current_node.data)
            for node in current_node.outbound_edges:
                if not node.visited:
                    node.visited = True
                    q.append(node)


if __name__ == '__main__':
    adjacency_list = {
        0: [2,6],
        1: [4],
        2: [3],
        3: [5],
        4: [],
        5: [6],
        6: [1]
    }
    g = Graph()
    ImplementGraph().create_graph(g, adjacency_list)
    ImplementGraph().print_graph_adjacency(g)
    print("Printing DFS")
    ImplementGraph().implement_dfs(g.node_list[0])
    ImplementGraph().reset_graph(g)
    print("Printing BFS")
    ImplementGraph().implement_bfs(g.node_list[0])
