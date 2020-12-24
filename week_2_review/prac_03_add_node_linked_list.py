class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = Node(value)

    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    def get_node(self, index):
        node = self.head
        count = 0
        while count < index:
            node = node.next
            count += 1
        return node

    def add_node(self, index, value):       # 전략: index-1번째와 index번째 node를 분리하고, 그 사이에 새로운 node를 입력한다.

        new_node = Node(value)              # 준비단계: 새로운 노드를 준비한다.
        if index == 0:
            new_node.next = self.head
            new_node = Node(value)
            next_node = node.next
            node


        node = self.get_node(index - 1)     # 준비단계: index-1번째 index에 접근한다.
        next_node = node.next               # 준비단계: index번째 이후 node(줄줄이 사탕)를 next_node 변수에 저장한다.
        node.next = new_node                # 체결: index -1 번째 노드와 새로운 index를 연결한다.
        new_node.next = next_node           # 체결: 새로운 노드와 index번째 이후 node를 모두 연결한다.



linked_list = LinkedList(5)
linked_list.append(12)
linked_list.add_node(0, 3)
linked_list.print_all()
