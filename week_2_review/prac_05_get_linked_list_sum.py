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


def get_linked_list_sum(linked_list_1, linked_list_2):

    sum_1 = linked_list_sum(linked_list_1)
    sum_2 = linked_list_sum(linked_list_2)

    return sum_1 + sum_2


def linked_list_sum(linked_list):
    cur = linked_list.head
    linked_sum = 0
    while cur is not None:
        linked_sum = linked_sum * 10 + cur.data
        cur = cur.next
    return linked_sum

# [6] -> [7] -> [8]
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(8)

# [3] -> [4] -> [5]
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)

print(get_linked_list_sum(linked_list_1, linked_list_2))
