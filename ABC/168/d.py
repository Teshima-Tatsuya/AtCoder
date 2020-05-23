class Node:
    def __init__(self, value, parent, depth):
        self.value = value
        self.parent = parent
        self.depth = depth


N, M = map(int, input().split())

root = Node(1, None, 0)
routes = []
for i in range(M):
    l = list(map(int, input().split()))
    l.sort()
    routes.append(l)

routes.sort()
for i in range(M):
    if routes[0] == 1:
        Node(routes[1], root, 1)

results = []
for i in range(2, M + 1):
    # 1にたどり着くまで
    while True:
        pass

# parent, depth
