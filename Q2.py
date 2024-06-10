class Watch:
    def __init__(self, code, make, size, price):
        self.code = code
        self.make = make
        self.size = size
        self.price = price

    def __repr__(self):
        return f"{self.code}, {self.make}, {self.size}, {'%.3f' % self.price}"


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class qNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class MyQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return self.head == None

    def enQueue(self, data):
        node = qNode(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def deQueue(self):
        if self.isEmpty():
            return None
        data = self.head.data
        self.head = self.head.next
        return data


class BSTree:
    def __init__(self):
        self.root = None

    def clear(self):
        self.root = None

    def isEmpty(self):
        return self.root == None

    def insert(self, data):
        self.root = BSTree.insertNode(self.root, data)

    def insertNode(node, data):
        if node is None:
            return Node(data)
        if data.code < node.data.code:
            node.left = BSTree.insertNode(node.left, data)
        elif data.code > node.data.code:
            node.right = BSTree.insertNode(node.right, data)
        return node

    def visit(self, p):
        if p == None:
            return
        print(f"{p.data}")

    def preOrder(self, p):
        if p == None:
            return
        self.visit(p)
        self.preOrder(p.left)
        self.preOrder(p.right)

    def preVisit(self):
        self.preOrder(self.root)
        print()

    def inOrder(self, p):
        if p == None:
            return
        self.inOrder(p.left)
        self.visit(p)
        self.inOrder(p.right)

    def inVisit(self):
        self.inOrder(self.root)
        print()

    def postOrder(self, p):
        if p == None:
            return
        self.postOrder(p.left)
        self.postOrder(p.right)
        self.visit(p)

    def postVisit(self):
        self.postOrder(self.root)
        print()

    def breadth_first(self):
        if self.isEmpty():
            return
        mq = MyQueue()
        mq.enQueue(self.root)
        while not mq.isEmpty():
            p = mq.deQueue()
            self.visit(p)
            if p.left != None:
                mq.enQueue(p.left)
            if p.right != None:
                mq.enQueue(p.right)

    

    # This function is used for Question 1
    def findHeight(self,root):
        if root == None:
            return -1
        height_left= self.findHeight(root.left)
        height_right= self.findHeight(root.right)
        return max(height_left, height_right)+1

    def f1(self):

        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        print(self.findHeight(self.root))

        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------

     # This function is used for Question 2
    def visit_price(self, p):
        if p == None:
            return
        if p.data.price > 3.5 and p.data.price < 8:
            print(f"{p.data}")
    def postOrder_price(self, p):
        if p == None:
            return
        self.postOrder_price(p.left)
        self.postOrder_price(p.right)
        self.visit_price(p)
    def f2(self):
        
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        self.postOrder_price(self.root.left)
        print()
        
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------

    # This function is used for Question 3
    def f3(self):
        
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        k = (self.findHeight(self.root))
        new_watch = Watch('OR-FGW01006W0', 'Orient', 15 * k, k + 1)
        self.insert(new_watch)
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.preVisit()

    # This function is used for Question 4
    def decrease_price(self,root):
        if root == None:
            return 0
        if root.data.make=="Seiko":
            root.data.price*=0.85

        self.decrease_price(root.right)
        self.decrease_price(root.left)
    def f4(self):
        
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        self.decrease_price(self.root)
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()

    # this function is used for Question 5
    def remove_leaf(self,node):
        if node is None:
            return None
        if node.left is None and node.right is None:
            return None
        node.left = self.remove_leaf(node.left)
        node.right = self.remove_leaf(node.right)
        return node

    def f5(self):
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------


        self.root.right = self.remove_leaf(self.root.right)
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.breadth_first()

    def most_node(self,root):
        current = root
        while current.right is not None:
            current = current.right
        return current

    def f6(self):
        tmp = self.most_node(self.root)
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        self.visit(tmp)

    def count_node(self,root):
        if root ==None:
            return 0
        count=0
        if root.data.price >5:
            count=1
        count+=self.count_node(root.right)
        count+=self.count_node(root.left)
        return count
    
    def f7(self):
        k = self.count_node(self.root)
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(k)

    def average(self,root):
        if root is None:
            return (0, 0)
        left_sum, left_count = self.average(root.left)
        right_sum, right_count = self.average(root.right)
        total_sum = root.data.size + left_sum + right_sum
        total_count = 1 + left_count + right_count
        return total_sum, total_count
    def f8(self):
        s,c = self.average(self.root)
        # ------------------------------------------------------------------------------
        # -------------------------- Start your code here ------------------------------
        # -------------------------- End your code here --------------------------------
        # ------------------------------------------------------------------------------
        print(s/c)

# ========================DO NOT EDIT GIVEN STATEMENTS IN THE MAIN FUNCTION.============================
# ===IF YOU CHANGE, THE GRADING SOFTWARE CAN NOT FIND THE OUTPUT RESULT TO SCORE, THUS THE MARK IS 0.===
def main():
    tree = BSTree()
    tree.insert(Watch('OR-FUNG8003D0', 'Orient', 40, 3.762))
    tree.insert(Watch('SK-SUR263P1', 'Seiko', 41, 3.555))
    tree.insert(Watch('CT-BM7466-81H', 'Citizen', 40, 7.590))
    tree.insert(Watch('CT-CA7060-88L', 'Citizen', 42, 8.540))
    tree.insert(Watch('SK-SUR211P1', 'Seiko', 42, 3.690))

    print("Do you want to run Q2?")
    print("1. Run f1()")
    print("2. Run f2()")
    print("3. Run f3()")
    print("4. Run f4()")
    print("5. Run f5()")
    print("6. Run f6()")
    print("7. Run f7()")
    print("8. Run f8()")

    n = int(input("Enter a number : "))

    if n == 1:
        print("OUTPUT:")
        tree.f1()

    if n == 2:
        print("OUTPUT:")
        tree.f2()

    if n == 3:
        print("OUTPUT:")
        tree.f3()

    if n == 4:
        print("OUTPUT:")
        tree.f4()

    if n == 5:
        print("OUTPUT:")
        tree.f5()

    if n == 6:
        print("OUTPUT:")
        tree.f6()

    if n == 7:
        print("OUTPUT:")
        tree.f7()

    if n == 8:
        print("OUTPUT:")
        tree.f8()

    # end main


# --------------------------------
if __name__ == "__main__":
    main()
# ============================================================