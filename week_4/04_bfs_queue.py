# 위의 그래프를 예시로 삼아서 인접 리스트 방식으로 표현했습니다!
graph = {
    1: [2, 3, 4],
    2: [1, 5],
    3: [1, 6, 7],
    4: [1, 8],
    5: [2, 9],
    6: [3, 10],
    7: [3],
    8: [4],
    9: [5],
    10: [6]
}


def bfs_queue(adj_graph, start_node):
    queue = [start_node]
    visited = []

    while queue:
        cur_node = queue.pop(0)
        visited.append(cur_node)
        for adj_node in adj_graph[cur_node]:
            if adj_node not in visited:
                queue.append(adj_node)
    # 1. stack = [1], visited = [], cur_node = 1
    # 2. stack = [], visited = [1], cur_node = 1
    # 3. stack = [2,3,4], visited = [1], cur_node = 1
    # 4. stack = [3,4], visited = [1,2]

    return visited


print(bfs_queue(graph, 1))  # 1 이 시작노드입니다!
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 이 출력되어야 합니다!
