# coding=gbk
class TreeNode():
    '''定义树节点'''
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right


class BinTree():
    '''创建完全二叉树'''
    def __init__(self):
        '''定义初始化函数'''
        self.root = None # 实例化根结点为None
        self.ls = [] #* 定义列表用来存储节点的地址

    def add(self, val):
        '''定义add方法向树结构中添加元素'''
        node = TreeNode(val)  # *实例化树节点
        if self.root == None:  # *若根结点为None，添加根结点，并将根节点的地址添加到self.ls中
            self.root = node
            self.ls.append(self.root)
        else:
            rootNode = self.ls[0] #* 将第一个元素设为根节点
            if rootNode.left == None: #* 若根结点的左子树为None，添加左节点，并将其地址值添加到self.ls中
                rootNode.left = node
                self.ls.append(rootNode.left)
            elif rootNode.right == None: #* 若根节点的右子树为None，添加右节点，并将其地址添加到self.ls中
                rootNode.right = node
                self.ls.append(rootNode.right)
                self.ls.pop(0) # ? 弹出self.ls第一个位置处的元素

    def preOrderTraversal(self, root):
        '''前序遍历（根左右），递归实现'''
        if root == None: #* 若 根节点为None，返回
            return
        print(root.val) #* 打印根节点的数据项
        self.preOrderTraversal(root.left)  # ? 对左子树递归调用前序遍历函数
        self.preOrderTraversal(root.right) # ? 对右子树递归调用前序遍历函数


    def preOrderStack(self, root):
        '''前序遍历（根左右）：堆栈实现'''
        if root == None: #* 定义空列表
            return
        stack = []
        result = []
        node = root
        while node or stack: # * 当node不为None或stack不为空时进入循环
            while node: # ? 寻找当前节点的左子树，并将其地址添加到stack中
                result.append(node.val) # * 将当前节点的数据项添加到result中
                stack.append(node)
                node = node.left # 当前节点不再有左子结点，退出被循环
            node = stack.pop() # * 将当前节点出stack，获取其地址值
            node = node.right # * 寻找当前节点的右子节点
        print(result) # 打印遍历结果

    def inOrderTraversal(self, root):
        '''中序遍历（左跟右）：递归实现'''
        if root == None:
            return
        self.inOrderTraversal(root.left) # * 对左子树递归调用中序遍历函数
        print(root.val) # * 打印当前节点的数据项
        self.inOrderTraversal(root.right) # * 对右子树递归调用中序遍历函数

    def inOrderStack(self, root):
        '''中序遍历（左跟右） 堆栈实现'''
        if root == None:
            return
        stack = []
        result = []
        node = root
        while node or stack:
            while node:  # * 若当前节点不为None，将其添加到stack中
                stack.append(node)
                node = node.left # * 寻找当且节点的左子节点，直到当前节点无左子节点跳出内循环
            node = stack.pop() # * 将当前节点pop出stack获取当前节点的地址值
            result.append(node.val) # * 将当前节点的数据项添加都按result中
            node = node.right # * 寻找当前节点的右子节点
        print(result)

    def postOrderTraversal(self, root):
        '''后续遍历（左右根） 递归实现'''
        if root == None:
            return
        self.postOrderTraversal(root.left) # * 对左子树递归调用后续函数
        self.postOrderTraversal(root.right) # * 对右子树递归调用后续函数
        print(root.val)

    def postOrderStack(self, root):
        '''
        后序遍历（左右根），堆栈实现，后序遍历的访问顺序（左右根）可以看做将
        先序遍历顺序（根左右）改为（根右左）后的逆序
        '''
        if root == None:
            return
        stack = []
        seq = []
        result = []
        node = root
        while node or stack:
            while node: # * 若当前节点不为None，将其添加到stack
                seq.append(node.val) # * 将当前节点的数据项添加到seq中
                stack.append(node)
                node = node.right # * 寻找当前节点的所有子结点，若当前节点五左右子结点，跳出内循环
            node = stack.pop() # 将当前节点pop出stack获取当前节点的地址值
            node = node.left # 寻找当前节点的左子节点
        while seq: # ? 若seq不为[]，将seq中的元素逆序添加到result中
            result.append(seq.pop())
        print(result)

    def levelOrder(self, root):
        '''
        层次遍历，广度优先遍历
        '''
        if root ==  None:
            return
        queue = [] # * 创建队列
        result = []
        node = root
        queue.append(node)  # 根结点入队

        while queue: # 若队列不为空
            node = queue.pop(0) # 当前节点出队
            result.append(node.val)  # 访问当前节点的数据项，并将其添加都按result中
            if node.left != None:  # 若左节点非空，左节点入队
                queue.append(node.left)
            if node.right != None: # 有节点非空，有节点入队
                queue.append(node.right)
        print(result)

    def printLeafNode(self, root):
        '''打印二叉树的叶子节点'''
        if root == None:
            return
        # ?只有当当前节点为叶子节点时打印当前的数据项
        if (root.left == None) and (root.right == None):
            print(root.data)
        self.printLeafNode(root.left)
        self.printLeafNode(root.right)

    # ! 求二叉树的高度
    def heightOfBT(self, root):
        '''求二叉树的高度'''
        if root == None:
            return 0
        HL = self.heightOfBT(root.left)
        HR = self.heightOfBT(root.right)
        if HL > HR:
            return HL + 1
        else:
            return HR + 1







if __name__ == '__main__':
    tree = BinTree() #* 实例化树对象
    for i in range(1, 11): #* 向树节点中添加元素1-10
        tree.add(i)
    # tree.preOrderStack(tree.root)
    # tree.preOrderTraversal(tree.root)
    print('指导青年')
    print(tree.heightOfBT(tree.root))


