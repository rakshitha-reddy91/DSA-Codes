#stack implementation using list
# stack = []
# def push():
#     element = int(input("Enter the element"))
#     stack.append(element)
#     print("element pushed into stack",element)
# def pop():
#     if not stack:
#         print("Stack is empty")
#     else:
#         print("Popped element:",stack.pop())
# def peek():
#     if not stack:
#         print("Stack is empty")
#     else:
#         print("Peek element is:",stack[-1])
# def  display():
#     if not stack:
#         print("Stack is empty")
#     else:
#         print("The elements in stack:",stack[::-1])
# while True:
#     print("Select the operation 1.push 2.pop 3.peek 4.display 5.exit")
#     choice = int(input())
#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop()
#     elif choice == 3:
#         peek()
#     elif choice == 4:
#         display()
#     elif choice == 5:
#         break
#     else:
#         print("Invalid choice")
#using isEmpty and isFull functions
# stack = []
# MAX = 5

# # Check if stack is empty
# def isEmpty():
#     return len(stack) == 0

# # Check if stack is full
# def isFull():
#     return len(stack) == MAX

# # Push operation
# def push():
#     if isFull():
#         print("Stack is full")
#     else:
#         element = int(input("Enter element to push: "))
#         stack.append(element)
#         print(element, "pushed into stack")

# # Pop operation
# def pop():
#     if isEmpty():
#         print("Stack is empty")
#     else:
#         print("Popped element:", stack.pop())

# # Display operation
# def display():
#     if isEmpty():
#         print("Stack is empty")
#     else:
#         print("Stack elements:", stack[::-1])

# # Main program
# while True:
#     print("\n1. Push")
#     print("2. Pop")
#     print("3. Display")
#     print("4. Is Empty")
#     print("5. Is Full")
#     print("6. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         push()
#     elif choice == 2:
#         pop()
#     elif choice == 3:
#         display()
#     elif choice == 4:
#         print("Stack is empty" if isEmpty() else "Stack is not empty")
#     elif choice == 5:
#         print("Stack is full" if isFull() else "Stack is not full")
#     elif choice == 6:
#         print("Exiting program")
#         break
#     else:
#         print("Invalid choice")
# stack = []
# def push(item):
#     stack.append(item)
#     print(f"Pushed {item} to stack: {stack}")
# def pop():
#     item = stack.pop()
#     print(f"Popped {item} from stack: {stack}")
# def peek():
#     print(f"Top item is: {stack[-1]}")
# def isEmpty():
#     return len(stack) == 0
# def size():
#     return len(stack)
# push(1)
# push(2)
# push(3)
# peek()
# pop()
#stack implementation using linked list
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class Stack:
#     def __init__(self):
#         self.top = None

#     def isEmpty(self):
#         return self.top is None

#     def isFull(self):
#         return False

#     # Insert at beginning
#     def push(self, data):
#         if self.isFull():
#             print("Stack is full")
#         else:
#             new_node = Node(data)
#             new_node.next = self.top
#             self.top = new_node
#             print(data, "pushed into stack")

#     # Delete at beginning
#     def pop(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Popped element:", self.top.data)
#             self.top = self.top.next

#     def peek(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             print("Top element:", self.top.data)

#     def display(self):
#         if self.isEmpty():
#             print("Stack is empty")
#         else:
#             temp = self.top
#             print("Stack elements:", end=" ")
#             while temp:
#                 print(temp.data, end=" ")
#                 temp = temp.next
#             print()


# s = Stack()

# while True:
#     print("\n1. Push")
#     print("2. Pop")
#     print("3. Peek")
#     print("4. Display")
#     print("5. Is Empty")
#     print("6. Is Full")
#     print("7. Exit")

#     choice = int(input("Enter your choice: "))

#     if choice == 1:
#         data = int(input("Enter element: "))
#         s.push(data)
#     elif choice == 2:
#         s.pop()
#     elif choice == 3:
#         s.peek()
#     elif choice == 4:
#         s.display()
#     elif choice == 5:
#         print("Stack is empty" if s.isEmpty()
#               else "Stack is not empty")
#     elif choice == 6:
#         print("Stack is full" if s.isFull()
#               else "Stack is not full")
#     elif choice == 7:
#         print("Exiting program")
#         break
#     else:
#         print("Invalid choice")
# class Solution:
#     def calPoints(self, operations: list[str]) -> int:
#         stack = []
#         for i in operations:
#             if i == 'C':
#                 stack.pop()
#             elif i == 'D':
#                 stack.append(stack[-1]*2)
#             elif i == '+':
#                 stack.append(stack[-1]+stack[-2])
#             else:
#                 stack.append(int(i))
#         return sum(stack)
#stack operations geeksforGeeks
# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
# class MyStack:
#     def __init__(self):
#         self.top = None
#         self.size = 0
        
        

#     def push(self, x):
#         new_node = Node(x)
#         new_node.next = self.top
#         self.top = new_node
#         self.size += 1

#     def pop(self):
#         if self.isEmpty():
#             return
#         self.top = self.top.next
#         self.size -= 1

#     def peek(self):
#         if self.isEmpty():
#             return -1
#         return self.top.data

#     def getSize(self):
#         return self.size

#     def isEmpty(self):
#         return self.top is None
#leetcodde 1614
# def maxDepth(self, s: str) -> int:
#         d = 0
#         m_d = 0
#         for ch in s:
#             if ch == '(':
#                 d += 1
#                 m_d = max(m_d,d)
#             elif ch == ')':
#                 d -= 1
#         return m_d
#leetcode 682
# operations = ["5","2","C","D","+"]
# stack = []
# for i in operations:
#     if i == 'C':
#         stack.pop()
#     elif i == 'D':
#         stack.append(stack[-1]*2)
#     elif i == '+':
#         stack.append(stack[-1]+stack[-2])
#     else:
#         stack.append(int(i))
# print(sum(stack))
#leetcode 1544
# s = "leEeetcode"
# stack = []
# for i in s:
#     if stack and stack[-1].lower()==i.lower() and stack[-1]!=i:
#         stack.pop()
#     else:
#         stack.append(i)
# print('' .join(stack))
#leetcode 1047
# s = "abbaca"
# stack = []
# for i in s:
#     if stack and stack[-1].lower() == i.lower():
#         stack.pop()
#     else:
#         stack.append(i)
# print(''.join(stack))
#leetcode 1441  
# target = [1,3] 
# n = 3
# result = []
# for i in range(1,target[-1]+1):
#     result.append("Push")
#     if i not in target:
#         result.append("Pop")
# print(result)
#leetcode 20

# s = input("Enter brackets: ")

# stack = []

# pairs = {
#     ')': '(',
#     '}': '{',
#     ']': '['
# }

# valid = True

# for ch in s:
#     if ch in "({[":
#         stack.append(ch)
#     else:
#         if not stack or stack[-1] != pairs[ch]:
#             valid = False
#             break
#         stack.pop()

# if len(stack) != 0:
#     valid = False

# print(valid)
#leetcode 75
# nums = [2,0,2,1,1,0]
# low = 0
# mid = 0
# high = len(nums)-1
# while mid <= high:
#     if nums[mid] == 0:
#         nums[low],nums[mid]=nums[mid],nums[low]
#         low+=1
#         mid+=1
#     elif nums[mid] == 1:
#         mid+=1
#     else:
#         nums[mid],nums[high] = nums[high],nums[mid]
#         high -= 1
# print(nums)
#leetcode 57

# intervals = [[1,3],[6,9]]
# newInterval = [2,5]
# n = len(intervals)
# i = 0
# result = []
# while i<n and intervals[i][1]<newInterval[0]:
#     result.append(intervals[i])
#     i+=1
# while i<n and intervals[i][0]<= newInterval[1]:
#     newInterval[0]=min(intervals[i][0],newInterval[0])
#     newInterval[1]=max(intervals[i][1],newInterval[1])
#     i+=1
# result.append(newInterval)
# while i<n:
#     result.append(intervals[i])
#     i+=1
# print(result)
#leetcode 16
# nums = [-1,2,1,-4] 
# target = 1
# nums.sort()
# closest = nums[0]+nums[1]+nums[2]
# for i in range(len(nums)-2):
#     left = i+1
#     right = len(nums)-1
#     while(left<right):
#         total = nums[i]+nums[left]+nums[right]
#         if abs(total-target)<abs(closest-target):
#             closest = total
#         if total == target:
#             closest = total
#             break
#         elif total<target:
#             left+=1
#         else:
#             right-=1
#     if closest == target:
#         break
# print(closest)
#leetcode 53
nums = [-2,1,-3,4,-1,2,1,-5,4]
c_s = nums[0]
m_s = nums[0]
for i in range(1,len(nums)):
    c_s = max(nums[i],c_s+nums[i])
    m_s = max(m_s,c_s)
print(m_s)
                
                 
        
        
        



        

    