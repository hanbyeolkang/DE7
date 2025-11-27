import sys
sys.setrecursionlimit(10**6)  # 재귀 횟수 최대 100만으로 증가

def solution(nodeinfo):
    class Node:
        def __init__(self, num, x, y):
            self.num = num
            self.x = x
            self.y = y
            self.left = None
            self.right = None

    def insertNode(parent, child):
        if child.x < parent.x:
            if parent.left is None:
                parent.left = child
            else:
                insertNode(parent.left, child)
        else:
            if parent.right is None:
                parent.right = child
            else:
                insertNode(parent.right, child)

    preorderList = []   # 전위 순회
    def preorder(node):
        if node is None:
            return
        preorderList.append(node.num)
        preorder(node.left)
        preorder(node.right)
    
    postorderList = []  # 후위 순회
    def postorder(node):
        if node is None:
            return
        postorder(node.left)
        postorder(node.right)
        postorderList.append(node.num)


    nodeinfo = [[i+1, x, y] for i, [x, y] in enumerate(nodeinfo)]   # [num, x, y]
    nodeinfo.sort(key=lambda x: (-x[2], x[1]))  # order by y desc, x asc

    root = Node(*nodeinfo[0])   # 앞에 * 붙여야 num, x, y 변수로 각각 전달됨
    for node in nodeinfo[1:]:   # root 노드는 제외
        insertNode(root, Node(*node)) # 여기도 * 주의

    preorder(root)
    postorder(root)
    
    return [preorderList, postorderList]


nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]
print(solution(nodeinfo))   # 예상 결과 : [[7,4,6,9,1,8,5,2,3],[9,6,5,8,1,4,3,2,7]]

# https://school.programmers.co.kr/learn/courses/30/lessons/42892