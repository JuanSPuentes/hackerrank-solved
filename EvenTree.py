""" Even Tree
https://www.hackerrank.com/challenges/even-tree/problem """

# Complete the evenForest function below.
def evenForest(t_nodes, t_edges, t_from, t_to) -> int:
    """
    Returns the number of edges to be removed to create a forest of even trees.

    Args:
        t_nodes (int): Number of nodes in the tree.
        t_edges (int): Number of edges in the tree.
        t_from (list): List of source nodes for each edge.
        t_to (list): List of destination nodes for each edge.

    Returns:
        int: Number of edges to be removed.
    """

    adj_list = {i: [] for i in range(1, t_nodes + 1)}

    for i in range(t_edges):
        adj_list[t_from[i]].append(t_to[i])
        adj_list[t_to[i]].append(t_from[i])

    count = [1] * (t_nodes + 1)
    edges_removed = 0

    def dfs(node, parent):
        """ Depth-first search """
        nonlocal edges_removed
        for child in adj_list[node]:
            if child != parent:
                dfs(child, node)
                count[node] += count[child]
                if count[child] % 2 == 0:
                    edges_removed += 1

    dfs(1, 0)
    return edges_removed

if __name__ == '__main__':
    t_nodes = 10
    t_edges = 9
    t_from = [2, 3, 4, 5, 6, 7, 8, 9, 10]
    t_to = [1, 1, 3, 2, 1, 2, 6, 8, 8]
    result = evenForest(t_nodes, t_edges, t_from, t_to)
    print(result)  # 2