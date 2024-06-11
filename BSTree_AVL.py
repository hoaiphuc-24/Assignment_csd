class Node:
    def __init__(self, key):
        self.rChild = None
        self.lChild = None
        self.key = key


class BSTree:
    def __init__(self):
        self.root = None

    def insertRec(self, tmp, new_number):
        if (tmp == None):
            tmp = Node(new_number)
        elif (new_number < tmp.key):
            tmp.lChild = self.insertRec(tmp.lChild, new_number)
        elif (new_number > tmp.key):
            tmp.rChild = self.insertRec(tmp.rChild, new_number)
        return tmp

    def insert(self, new_number):
        self.root = self.insertRec(self.root, new_number)

    def preOrder(self, tmp):
        if (tmp != None):
            print(tmp.key)
            self.preOrder(tmp.lChild)
            self.preOrder(tmp.rChild)
    
    def printTree1(self):
        self.preOrder(self.root)

    def inOrder(self, tmp):
        if (tmp != None):
            self.inOrder(tmp.lChild)
            print(tmp.key)
            self.inOrder(tmp.rChild)

    def printTree2(self):
        # inorder
        self.inOrder(self.root)

    def printTree3(self):
        # postorder
        pass

    def printTree4(self):
        # breadth first traversal
        pass

    def search(self, k):
        self.searchRec(self.root, k)

    def searchRec(self, tmp, k):
        if (tmp == None):
            return False
        else:
            if (tmp.key == k):
                return True
            elif (tmp.key > k):
                return self.searchRec(tmp.lChild, k)
            else:
                return self.searchRec(tmp.rChild, k)

    def findFather(self, k):
        pass

    def calHeight(self):
        pass

    def countLeaf(self):
        return self.countLeafRec(self.root)

    def countLeafRec(self, tmp):
        if (tmp == None):
            return 0
        # node dang xet la mot node "leaf"
        if (tmp.lChild == None and tmp.rChild == None):
            return 1
        else:  # node khong phai "leaf"
            return self.countLeafRec(tmp.lChild) + self.countLeafRec(tmp.rChild)

    def printLeaf(self):
        return self.printLeafRec(self.root)

    def printLeafRec(self, tmp):
        if (tmp == None):
            return
        # node dang xet la mot node "leaf"
        if (tmp.lChild == None and tmp.rChild == None):
            print(tmp.key)
        self.printLeafRec(tmp.lChild)
        self.printLeafRec(tmp.rChild)

    def sum(self):
        return self.sumRec(self.root)

    def sumRec(self, tmp):
        if (tmp == None):
            return 0
        return self.sumRec(tmp.lChild) + tmp.key + self.sumRec(tmp.rChild)

    def countNode(self):
        return self.countNodeRec(self.root)

    def countNodeRec(self, tmp):
        if (tmp == None):
            return 0
        return self.countNodeRec(tmp.lChild) + 1 + self.countNodeRec(tmp.rChild)

    def delete(self, k):
        pass

    def deleteLeaf(self, k):
        pass
        
    def deleteNodeWithOneChild(self, k):
        pass
        
    # ======================================================
    # Some extensions for AVL Trees
    def calBalanceFactor(self, n):
        pass

    def sleftRotate(self, n):
        # single left rotation
        pass

    def srightRotate(self, n):
        # single right rotation
        pass

    def dleftRotate(self, n):
        # double left rotation
        pass

    def drightRotate(self, n):
        # double right rotation
        pass

    def doBalancing(self, n):
        pass
        
    def AVLDeleteNode(self, n):
        pass
        
    def AVLInsertNode(self, n):
        pass


def processing():
    t = BSTree()
    t.insert(15)
    t.insert(8)
    t.insert(25)
    t.insert(13)
    t.insert(5)
    t.insert(20)
    t.insert(30)
    t.insert(3)
    t.printTree2()
    print("Amount of Nodes:  ", t.countNode())
    k = 20
    if (t.search(k) == True):
        print("Node ", k, " is in the BSTree")
    else:
        print("Node ", k, " is not in the BSTree")
    # test some functions here
    print("Amount of leaf nodes:  ", t.countLeaf())
    print("List of leaf: ")
    t.printLeaf()
    print("Sum of nodes:  ", t.sum())


if __name__ == '__main__':
    processing()