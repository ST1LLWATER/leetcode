class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def zigzag(root):
    if root is None:
        return
    ans=[]
    current_level = [root]
    next_level = []
    while current_level or next_level:
        current=[]
        if current_level:
            while current_level:
                node = current_level.pop()
                current.append(node.value)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        else:
            while next_level:
                node = next_level.pop()
                current.append(node.value)
                if node.right:
                    current_level.append(node.right)
                if node.left:
                    current_level.append(node.left)

        ans.append(current)
    
    print(ans)

root=Node(3)
root.left=Node(9)
root.right=Node(20)
root.right.left=Node(15)
root.right.right=Node(7)

zigzag(root)
