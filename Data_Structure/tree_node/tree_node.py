# coding=gbk
class TreeNode():
    '''�������ڵ�'''
    def __init__(self, val, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right


class BinTree():
    '''������ȫ������'''
    def __init__(self):
        '''�����ʼ������'''
        self.root = None # ʵ���������ΪNone
        self.ls = [] #* �����б������洢�ڵ�ĵ�ַ

    def add(self, val):
        '''����add���������ṹ�����Ԫ��'''
        node = TreeNode(val)  # *ʵ�������ڵ�
        if self.root == None:  # *�������ΪNone����Ӹ���㣬�������ڵ�ĵ�ַ��ӵ�self.ls��
            self.root = node
            self.ls.append(self.root)
        else:
            rootNode = self.ls[0] #* ����һ��Ԫ����Ϊ���ڵ�
            if rootNode.left == None: #* ��������������ΪNone�������ڵ㣬�������ֵַ��ӵ�self.ls��
                rootNode.left = node
                self.ls.append(rootNode.left)
            elif rootNode.right == None: #* �����ڵ��������ΪNone������ҽڵ㣬�������ַ��ӵ�self.ls��
                rootNode.right = node
                self.ls.append(rootNode.right)
                self.ls.pop(0) # ? ����self.ls��һ��λ�ô���Ԫ��

    def preOrderTraversal(self, root):
        '''ǰ������������ң����ݹ�ʵ��'''
        if root == None: #* �� ���ڵ�ΪNone������
            return
        print(root.val) #* ��ӡ���ڵ��������
        self.preOrderTraversal(root.left)  # ? ���������ݹ����ǰ���������
        self.preOrderTraversal(root.right) # ? ���������ݹ����ǰ���������


    def preOrderStack(self, root):
        '''ǰ������������ң�����ջʵ��'''
        if root == None: #* ������б�
            return
        stack = []
        result = []
        node = root
        while node or stack: # * ��node��ΪNone��stack��Ϊ��ʱ����ѭ��
            while node: # ? Ѱ�ҵ�ǰ�ڵ�����������������ַ��ӵ�stack��
                result.append(node.val) # * ����ǰ�ڵ����������ӵ�result��
                stack.append(node)
                node = node.left # ��ǰ�ڵ㲻�������ӽ�㣬�˳���ѭ��
            node = stack.pop() # * ����ǰ�ڵ��stack����ȡ���ֵַ
            node = node.right # * Ѱ�ҵ�ǰ�ڵ�����ӽڵ�
        print(result) # ��ӡ�������

    def inOrderTraversal(self, root):
        '''�������������ң����ݹ�ʵ��'''
        if root == None:
            return
        self.inOrderTraversal(root.left) # * ���������ݹ���������������
        print(root.val) # * ��ӡ��ǰ�ڵ��������
        self.inOrderTraversal(root.right) # * ���������ݹ���������������

    def inOrderStack(self, root):
        '''�������������ң� ��ջʵ��'''
        if root == None:
            return
        stack = []
        result = []
        node = root
        while node or stack:
            while node:  # * ����ǰ�ڵ㲻ΪNone��������ӵ�stack��
                stack.append(node)
                node = node.left # * Ѱ�ҵ��ҽڵ�����ӽڵ㣬ֱ����ǰ�ڵ������ӽڵ�������ѭ��
            node = stack.pop() # * ����ǰ�ڵ�pop��stack��ȡ��ǰ�ڵ�ĵ�ֵַ
            result.append(node.val) # * ����ǰ�ڵ����������Ӷ���result��
            node = node.right # * Ѱ�ҵ�ǰ�ڵ�����ӽڵ�
        print(result)

    def postOrderTraversal(self, root):
        '''�������������Ҹ��� �ݹ�ʵ��'''
        if root == None:
            return
        self.postOrderTraversal(root.left) # * ���������ݹ���ú�������
        self.postOrderTraversal(root.right) # * ���������ݹ���ú�������
        print(root.val)

    def postOrderStack(self, root):
        '''
        ������������Ҹ�������ջʵ�֣���������ķ���˳�����Ҹ������Կ�����
        �������˳�򣨸����ң���Ϊ�������󣩺������
        '''
        if root == None:
            return
        stack = []
        seq = []
        result = []
        node = root
        while node or stack:
            while node: # * ����ǰ�ڵ㲻ΪNone��������ӵ�stack
                seq.append(node.val) # * ����ǰ�ڵ����������ӵ�seq��
                stack.append(node)
                node = node.right # * Ѱ�ҵ�ǰ�ڵ�������ӽ�㣬����ǰ�ڵ��������ӽ�㣬������ѭ��
            node = stack.pop() # ����ǰ�ڵ�pop��stack��ȡ��ǰ�ڵ�ĵ�ֵַ
            node = node.left # Ѱ�ҵ�ǰ�ڵ�����ӽڵ�
        while seq: # ? ��seq��Ϊ[]����seq�е�Ԫ��������ӵ�result��
            result.append(seq.pop())
        print(result)

    def levelOrder(self, root):
        '''
        ��α�����������ȱ���
        '''
        if root ==  None:
            return
        queue = [] # * ��������
        result = []
        node = root
        queue.append(node)  # ��������

        while queue: # �����в�Ϊ��
            node = queue.pop(0) # ��ǰ�ڵ����
            result.append(node.val)  # ���ʵ�ǰ�ڵ���������������Ӷ���result��
            if node.left != None:  # ����ڵ�ǿգ���ڵ����
                queue.append(node.left)
            if node.right != None: # �нڵ�ǿգ��нڵ����
                queue.append(node.right)
        print(result)

    def printLeafNode(self, root):
        '''��ӡ��������Ҷ�ӽڵ�'''
        if root == None:
            return
        # ?ֻ�е���ǰ�ڵ�ΪҶ�ӽڵ�ʱ��ӡ��ǰ��������
        if (root.left == None) and (root.right == None):
            print(root.data)
        self.printLeafNode(root.left)
        self.printLeafNode(root.right)

    # ! ��������ĸ߶�
    def heightOfBT(self, root):
        '''��������ĸ߶�'''
        if root == None:
            return 0
        HL = self.heightOfBT(root.left)
        HR = self.heightOfBT(root.right)
        if HL > HR:
            return HL + 1
        else:
            return HR + 1







if __name__ == '__main__':
    tree = BinTree() #* ʵ����������
    for i in range(1, 11): #* �����ڵ������Ԫ��1-10
        tree.add(i)
    # tree.preOrderStack(tree.root)
    # tree.preOrderTraversal(tree.root)
    print('ָ������')
    print(tree.heightOfBT(tree.root))


