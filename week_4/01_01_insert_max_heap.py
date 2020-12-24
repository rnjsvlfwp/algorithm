class MaxHeap:
    def __init__(self):
        self.items = [None]

    def insert(self, value):
        # 1. 마지막에 노드를 추가한다.
        self.items.append(value)
        # 2. parent 노드와 비교한다.
        cur_index = len(self.items) - 1
        while cur_index > 1:
            parent_index = cur_index // 2
            if self.items[cur_index] > self.items[parent_index]:
                self.items[parent_index], self.items[cur_index] = self.items[cur_index], self.items[parent_index]
                cur_index = parent_index
            else:
                break



max_heap = MaxHeap()
max_heap.insert(3)
max_heap.insert(4)
max_heap.insert(2)
max_heap.insert(9)
print(max_heap.items)  # [None, 9, 4, 2, 3] 가 출력되어야 합니다!
