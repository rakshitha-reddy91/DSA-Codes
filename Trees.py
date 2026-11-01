#Binary trees
# class Node:
#     def __init__(self,data):
#         self.data=data
#         self.left = None
#         self.right = None
# class Binarytrees:
#     index = -1
#     def buildtree(self,l1):
#         self.index+=1
#         if l1[self.index] == -1:
#             return None
#         nn = Node(l1[self.index])
#         nn.left = self.buildtree(l1)
#         nn.right = self.buildtree(l1)
#         return nn
# l1 = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
# t1 = Binarytrees()
# root = t1.buildtree(l1)
# print(root.data)
#Traversal techniques
#Inorder traversal
# class Node:
    
#     def __init__(self,data):
#          self.data=data
#          self.left = None
#          self.right = None
# class Binarytrees:
#     index = -1
#     def buildtree(self,l1):
#         self.index+=1
#         if l1[self.index] == -1:
#             return None
#         nn = Node(l1[self.index])
#         nn.left = self.buildtree(l1)
#         nn.right = self.buildtree(l1)
#         return nn
#     def inorder(self,root):
#         if root is None:
#             return
#         self.inorder(root.left)
#         print(root.data,end=" ")
#         self.inorder(root.right)
# l1 = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
# t1 = Binarytrees()
# root = t1.buildtree(l1)
# print(root.data)
# print("Inorder Traversal:")
# t1.inorder(root)
#preorder
# class Node:
    
#     def __init__(self,data):
#         self.data=data
#         self.left = None
#         self.right = None
# class Binarytrees:
#     index = -1
#     def buildtree(self,l1):
#         self.index+=1
#         if l1[self.index] == -1:
#             return None
#         nn = Node(l1[self.index])
#         nn.left = self.buildtree(l1)
#         nn.right = self.buildtree(l1)
#         return nn
#     def preorder(self,root):
#         if root is None:
#             return
#         print(root.data,end=" ")
#         self.preorder(root.left)
#         self.preorder(root.right)
# l1 = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
# t1 = Binarytrees()
# root = t1.buildtree(l1)
# print(root.data)
# print("preorder Traversal:")
# t1.preorder(root)
#post order
# class Node:
    
#     def __init__(self,data):
#         self.data=data
#         self.left = None
#         self.right = None
# class Binarytrees:
#     index = -1
#     def buildtree(self,l1):
#         self.index+=1
#         if l1[self.index] == -1:
#             return None
#         nn = Node(l1[self.index])
#         nn.left = self.buildtree(l1)
#         nn.right = self.buildtree(l1)
#         return nn
#     def postorder(self,root):
#         if root is None:
#             return
#         self.postorder(root.left)
#         self.postorder(root.right)
#         print(root.data,end=" ")
# l1 = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
# t1 = Binarytrees()
# root = t1.buildtree(l1)
# print(root.data)
# print("postorder Traversal:")
# t1.postorder(root)
#level order
#binary search
class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class Binarytrees:
    index=-1
    def buildtree(self,l1):
        self.index+=1

        if l1[self.index]==-1:
            return None
        nn=Node(l1[self.index])
        nn.left=self.buildtree(l1)
        nn.right=self.buildtree(l1)

        return nn
    def inorder(self,root):
        if root is None:
            return 
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)
    def preorder(self,root):
        if root is None:
            return 
        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)
    def postorder(self,root):
        if root is None:
            return 
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")
    def levelorder(self,root):
        if root is None:
            return 
        queue=[]
        queue.append(root)
        queue.append(None)

        while queue:
            curr=queue.pop(0)
            if curr is None:
                if len(queue)==0:
                    break
                else:
                    queue.append(None)
                    print()
            else:
                print(curr.data, end=" ")
                if curr.left:
                    queue.append(curr.left)
                if curr.right :
                    queue.append(curr.right)


l1=[1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
t1=Binarytrees()
root=t1.buildtree(l1)
print(root.data)
print("indorder traversal:")
t1.inorder(root)
print()
print("preorder traversal")
t1.preorder(root)
print()
print("postorder traversal")
t1.postorder(root)
print()
print("level order traversal")
t1.levelorder(root)
              