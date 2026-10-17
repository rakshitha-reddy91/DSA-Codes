#to print the elements of linked list
# arr = list(map(int, input("Enter elements: ").split()))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = None
# temp = None

# for x in arr:
#     new_node = Node(x)

#     if head is None:
#         head = new_node
#         temp = head
#     else:
#         temp.next = new_node
#         temp = temp.next

# result = []
# temp = head

# while temp is not None:
#     result.append(temp.data)
#     temp = temp.next
# print(result)
# arr = list(map(int, input("Enter elements: ").split()))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = None
# temp = None

# for x in arr:
#     new_node = Node(x)

#     if head is None:
#         head = new_node
#         temp = head
#     else:
#         temp.next = new_node
#         temp = temp.next

# result = []
# temp = head

# while temp is not None:
#     result.append(temp.data)
#     temp = temp.next

# print(result)
# temp = head
# while temp is not None:
#     print(temp.data,end=" ")
#     temp = temp.next    
#to find the length of linked list
# arr = list(map(int, input("Enter elements: ").split()))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = None
# temp = None

# for x in arr:
#     new_node = Node(x)

#     if head is None:
#         head = new_node
#         temp = head
#     else:
#         temp.next = new_node
#         temp = temp.next

# count = 0
# temp = head
# while temp is not None:
#     count += 1
#     temp = temp.next
# print(count)
#to find the length of linked list even or odd
# arr = list(map(int, input("Enter elements: ").split()))

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# head = None
# temp = None

# for x in arr:
#     new_node = Node(x)

#     if head is None:
#         head = new_node
#         temp = head
#     else:
#         temp.next = new_node
#         temp = temp.next

# count = 0
# temp = head
# while temp is not None:
#     count +=1
#     temp = temp.next
# if count % 2 == 0:
#     print("Even")
# else:
#     print("Odd")
#remove elements from linked list
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

arr = list(map(int, input("Enter list elements: ").split()))
val = int(input("Enter value to remove: "))

head = None
temp = None

for x in arr:
    new_node = ListNode(x)

    if head is None:
        head = new_node
        temp = new_node
    else:
        temp.next = new_node
        temp = new_node
while head is not None and head.val == val:
    head = head.next
current = head
while current is not None and current.next is not None:
    if current.next.val == val:
        current.next = current.next.next
    else:
        current = current.next
temp = head
while temp is not None:
    print(temp.val,end = " ")
    temp =temp.next
    