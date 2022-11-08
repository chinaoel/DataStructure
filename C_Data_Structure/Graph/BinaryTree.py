from queue import Queue

class BinaryNode():
    def __init__(self,data,lchild=None,rchild=None):
        self.data = data
        self.lchild = lchild
        self.rchild = rchild



class BinaryTree():
    def __init__(self, root):
        self.root = root


    def addNode(self,data,root):
        if not root:
            return BinaryNode(data)
        
        if (data > root.data):
            root.rchild = self.addNode(data,root.rchild)
        elif (data < root.data):
            root.lchild = self.addNode(data,root.lchild)
        return root

    def LevelOrderTraversal(self):
        print(self.root.data)
        Q = Queue()
        Q.put(self.root)

        while (not Q.empty()):
            root = Q.get()
            if (root.lchild):
                print(root.lchild.data)
                Q.put(root.lchild)
            if (root.rchild):
                print(root.rchild.data)
                Q.put(root.rchild)

    def InOrder(self,root):
        if root:
            self.InOrder(root.lchild)
            print(root.data)
            self.InOrder(root.rchild)
        

if __name__ == '__main__':
    root = BinaryNode(10)
    tree = BinaryTree(root)
    tree.addNode(3,root)
    tree.addNode(7,root)
    tree.addNode(18,root)
    tree.addNode(20,root)
    tree.LevelOrderTraversal()

