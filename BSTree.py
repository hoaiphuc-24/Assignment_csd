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


    def preOrder(self,tmp):
        if tmp == None:
            return
        print(tmp.key)
        self.preOrder(tmp.lChild)
        self.preOrder(tmp.rChild)
    def printTree1(self):
        # preorder
        self.preOrder(self.root)

    def inOrder(self, tmp):
        if tmp ==None:
            return
        self.inOrder(tmp.lChild)
        print(tmp.key)
        self.inOrder(tmp.rChild)

    def printTree2(self):
        # inorder
        self.inOrder(self.root)

    def postOrder(self,tmp):
        if tmp == None:
            return
        self.postOrder(tmp.lChild)
        self.postOrder(tmp.rChild)
        print(tmp.key)
    def printTree3(self):
        # postorder
        self.postOrder(self.root, tmp)


    def breadth(self,tmp):
        if tmp== None :
            return
        queue=[]
        queue.append(tmp)

        while queue is not None:
            node=queue.pop(0)
            print(node.key)

            if node.lChild :
                queue.append(node.lChild)
            if node.rChild:
                queue.append(node.rChild)

    def printTree4(self):
        # breadth first traversal
        return self.breadth(self.root)

    def search(self, k):
        return self.searchRec(self.root, k)

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


    def find_father(self,tmp,k):
        if (tmp == None):
            return 0
        if tmp.key == k:
            return tmp.key
        if tmp.key> k:
            return find_father(tmp.rChild, k)
        else:
            return find_father(tmp.lChild, k)
        
    def findFather(self, k):
        print(self.find_father(self.root),k)



    def calH_Rec(self, tmp):
        if (tmp == None):
            return 0
        left_height= self.calH_Rec(tmp.lChild)
        right_height= self.calH_Rec(tmp.rChild)
        return max(left_height,right_height )
    def calHeight(self):
        print(self.calH_Rec(self.root))


    def countLeafRec(self,tmp):
        if (tmp == None):
            return 0
        if tmp.rChild==None and tmp.lChild==None:
            return 1
        return countLeafRec(tmp.rChild)+ countLeafRec(tmp.lChild)
    def countLeaf(self):
        print(self.countLeafRec(self.root))


    def sumRec(self,tmp):
        if (tmp == None):
            return 0
        return self.sumRec(tmp.rChild)+ tmp.key + self.sumRec(tmp.lChild)
    def sum(self):
        print( self.sumRec(self.root))

    def countNodeRec(self, tmp):
        if (tmp == None):
            return 0
        return self.countNodeRec(tmp.lChild) + 1 + self.countNodeRec(tmp.rChild)
    def countNode(self):
        print(self.countNodeRec(self.root))


    def deleteNode(self,tmp, k):
        if tmp ==None:
            return 0
        if k< tmp.key:
            tmp.lChild= self.deleteNode(tmp.lChild, k)
        elif k> tmp.key:
            tmp.rChild= self.deleteNode(tmp.rChild, k)
        else:
            # Node có 1 con hoặc ko con
            if tmp.lChild == None:
                return tmp.rChild
            elif tmp.rChild == None:
                return tmp.lChild
            #Node có 2 con
            value=self.minValue(tmp.rChild)
            tmp.key=value.key
            tmp.rChild= self.deleteNode(tmp.rChild, value.key)
        return tmp
    def minValue(self,r):
        minv= r
        while r.lChild is not None:
            minv= minv.lChild.key

        return minv
    def delete(self, k):
        return self.deleteNode(self.root, k)


    # ======================================================
    # Some extensions for AVL Trees
    def calBalanceFactor(self, n):
        if not n:
            return 0

        return self.calH_Rec(n.lChild) - self.calH_Rec(n.rChild)

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

    def doBalancing(self, n): #chuyển thành cây AVL
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
    t.insert(21)
    print("Amount of Nodes:  ", t.countNode())
    k = 20
    if (t.search(k) == True):
        print("Node ", k, " is in the BSTree")
    else:
        print("Node ", k, " is not in the BSTree")
    # test some functions here
    t.printTree4()


if __name__ == '__main__':
    processing()