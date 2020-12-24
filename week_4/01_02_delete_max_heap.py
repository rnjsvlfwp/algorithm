class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        self.items.append(value)
        cur_index = len(self.items) - 1

        while cur_index > 1:  # cur_index 가 1이 되면 정상을 찍은거라 다른 것과 비교 안하셔도 됩니다!
            parent_index = cur_index // 2
            if self.items[parent_index] < self.items[cur_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break

    def delete(self):
        # 1. 자리 변경: 루트 노드와 가장 마지막 노드의 자리를 변경한다.
        self.items[1], self.items[-1] = self.items[-1], self.items[1]
        # 2. 할당 및 삭제: 변경된 가장 마지막 노드를 다른 변수로 할당하고 삭제한다.
        prev_max = self.items.pop()
        cur_index = 1

        while cur_index < len(self.items) - 1:
            # 3. 비교1: 변경된 루트노드와 왼쪽 자식을 비교한다.
            left_node_index = cur_index * 2
            right_node_index = cur_index * 2 + 1
            if self.items[right_node_index] < self.items[left_node_index] and self.items[left_node_index] > self.items[
                cur_index]:
                self.items[cur_index], self.items[left_node_index] = self.items[left_node_index], self.items[cur_index]
                cur_index = left_node_index
            # 4. 비교2: 변경된 루트노드와 오른쪽 자식을 비교한다.
            elif self.items[right_node_index] > self.items[left_node_index] and self.items[right_node_index] > \
                    self.items[cur_index]:
                # 5. 자리 변경: 자식 노드 중 더 큰 자식과 자리를 변경한다.
                self.items[cur_index], self.items[right_node_index] = self.items[right_node_index], self.items[
                    cur_index]
                cur_index = right_node_index

        # 6. 종료 시점: 자식 노드가 없거나 자식 노드가 더 작을 때까지
        return prev_max


max_heap = MaxHeap()
max_heap.insert(8)
max_heap.insert(7)
max_heap.insert(6)
max_heap.insert(2)
max_heap.insert(5)
max_heap.insert(4)
print(max_heap.items)  # [None, 8, 7, 6, 2, 5, 4]
print(max_heap.delete())  # 8 을 반환해야 합니다!
print(max_heap.items)  # [None, 7, 5, 6, 2, 4]
