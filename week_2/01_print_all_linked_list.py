# 노드를 생성하는 함수
class Node:
    # 노드 생성 시 필요한 데이터는, 데이터 값과 다음 노드의 데이터 값 2가지다.
    def __init__(self, data):
        # 노드의 데이터 값
        self.data = data  # ex) Node(5)의 의미는 data에 5를 대입한다는 것이며, 이는 곧 자신의 데이터 깂이 5가 된다는 의미다.
        # 다음 노드의 데이터 값
        self.next = None  # 다음 노드 값은 None 이다.


# 연결된 linked list를 만드는 함수
class linkedList:
    # head 노드를 만드는 함수
    def __init__(self, value):  # ex) linkedList(5)의 의미는 value에 5를 대입한다는 것이며, 이는 곧 노드 생성 함수 data 값에 5가 대입되며
        self.head = Node(value)  # ex) 노드 생성 함수를 이용해 노드를 생성(다음 노드 포함)한뒤 head에 할당

    # 노드를 추가하는 함수
    def append(self, value):
        cur = self.head  # head 노드에 cur(current의 줄임)가 위치함

        while cur.next is not None:  # cur가 위치한 노드의 다음 노드 정보가 None이 아니라면
            cur = cur.next  # cur의 다음 노드 정보를 가진 노드로 cur를 이동시키기

        cur.next = Node(value)  # 맨 마지막에 append해주는 코드

    # 모든 노드를 현시하는 함수
    def print_all(self):
        cur = self.head  # head 노드에 cur(current의 줄임)가 위치함
        while cur.next is not None:  # cur가 위치한 노드의 다음 노드 정보가 None이 아니라면
            print(cur.data)  # cur의 현재 데이터를 현시하기
            cur = cur.next  # cur의 다음 노드 정보를 가진 노드로 cur를 이동시키기


linked_list = linkedList(5)
linked_list.append(12)
linked_list.append(8)
linked_list.print_all()
