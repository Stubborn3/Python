class node:
    def __init__(self):
        self.value = ""
        self.left = None
        self.right = None


class tree:
    
    def __init__(self):
        self.root = None

    def insertNode(self,temp, val):
        
        if temp.value == value:
            return

        if self.root == None:
            temp = node()
            temp.value = val
            temp.left = None
            temp.right = None
            self.root = temp
        elif temp.value < val:
            if temp.right == None:
                temp.right = node()
                temp.right.value = val
                temp.right.left = None
                temp.right.right = None
            else:
                self.insertNode(temp.right,val)

        elif temp.value > val:
            if temp.left == None:
                temp.left = node()
                temp.left.value = val
                temp.left.left = None
                temp.left.right = None
            else:
                self.insertNode(temp.left,val)

    def traverse(self,temp):
        if temp == None:
            return
        if temp.left != None:
            self.traverse(temp.left)
        if temp.right != None:
            self.traverse(temp.right)
        print(temp.value)

obj = tree()
obj.insertNode(obj.root,"5")
obj.insertNode(obj.root,"3")
obj.insertNode(obj.root,"2")
obj.traverse(obj.root)