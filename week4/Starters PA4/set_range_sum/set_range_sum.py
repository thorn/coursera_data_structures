# python3

from sys import stdin

# Splay tree implementation

# Vertex of a splay tree
class Vertex:
  def __init__(self, key, sum, left, right, parent):
    (self.key, self.sum, self.left, self.right, self.parent) = (key, sum, left, right, parent)

def update(v):
  if v == None:
    return
  v.sum = v.key + (v.left.sum if v.left != None else 0) + (v.right.sum if v.right != None else 0)
  if v.left != None:
    v.left.parent = v
  if v.right != None:
    v.right.parent = v

def smallRotation(v):
  parent = v.parent
  if parent == None:
    return
  grandparent = v.parent.parent
  if parent.left == v:
    m = v.right
    v.right = parent
    parent.left = m
  else:
    m = v.left
    v.left = parent
    parent.right = m
  update(parent)
  update(v)
  v.parent = grandparent
  if grandparent != None:
    if grandparent.left == parent:
      grandparent.left = v
    else:
      grandparent.right = v

def bigRotation(v):
  if v.parent.left == v and v.parent.parent.left == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  elif v.parent.right == v and v.parent.parent.right == v.parent:
    # Zig-zig
    smallRotation(v.parent)
    smallRotation(v)
  else:
    # Zig-zag
    smallRotation(v);
    smallRotation(v);

# Makes splay of the given vertex and makes
# it the new root.
def splay(v):
  if v == None:
    return None
  while v.parent != None:
    if v.parent.parent == None:
      smallRotation(v)
      break
    bigRotation(v)
  return v

# Searches for the given key in the tree with the given root
# and calls splay for the deepest visited node after that.
# Returns pair of the result and the new root.
# If found, result is a pointer to the node with the given key.
# Otherwise, result is a pointer to the node with the smallest
# bigger key (next value in the order).
# If the key is bigger than all keys in the tree,
# then result is None.
def find(root, key):
  v = root
  last = root
  next = None
  while v != None:
    if v.key >= key and (next == None or v.key < next.key):
      next = v
    last = v
    if v.key == key:
      break
    if v.key < key:
      v = v.right
    else:
      v = v.left
  root = splay(last)
  return (next, root)

def split(root, key):
  (result, root) = find(root, key)
  if result == None:
    return (root, None)
  right = splay(result)
  left = right.left
  right.left = None
  if left != None:
    left.parent = None
  update(left)
  update(right)
  return (left, right)


def merge(left, right):
  if left == None:
    return right
  if right == None:
    return left
  while right.left != None:
    right = right.left
  right = splay(right)
  right.left = left
  update(right)
  return right


# Code that uses splay tree to solve the problem

root = None

def insert(x):
  global root
  (left, right) = split(root, x)
  new_vertex = None
  if right == None or right.key != x:
    new_vertex = Vertex(x, x, None, None, None)
  root = merge(merge(left, new_vertex), right)

def erase(x):
  global root
  # Implement erase yourself
  (left, right) = split(root, x)
  (right1, right2) = split(right, x + 1)
  root = merge(left, right2)

def search(x):
  global root
  # Implement find yourself
  result, root = find(root, x)
  if not result: return False
  return result.key == x
  return False

def dosum(fr, to):
  global root
  (left, middle) = split(root, fr)
  (middle, right) = split(middle, to + 1)
  ans = 0
  if middle == None:
    root = merge(left, right)
    return 0
  ans = middle.sum
  root = merge(merge(left, middle), right)
  return ans

MODULO = 1000000001
n = int(stdin.readline())
last_sum_result = 0
for i in range(n):
  line = stdin.readline().split()
  if line[0] == '+':
    x = int(line[1])
    insert((x + last_sum_result) % MODULO)
  elif line[0] == '-':
    x = int(line[1])
    erase((x + last_sum_result) % MODULO)
  elif line[0] == '?':
    x = int(line[1])
    print('Found' if search((x + last_sum_result) % MODULO) else 'Not found')
  elif line[0] == 's':
    l = int(line[1])
    r = int(line[2])
    res = dosum((l + last_sum_result) % MODULO, (r + last_sum_result) % MODULO)
    print(res)
    last_sum_result = res % MODULO


# import random

# def print_result(operations):
#   for operation in operations:
#     print(operation)

# def random_test():
#     maxnumber = 10 #as you need
#     operations = []
#     values = []
#     while True:
#         op = random.randrange(5)
#         if op == 0 or op == 1:
#             arg = random.randrange(maxnumber) + 1
#             insert(arg)
#             operations.append("insert(" + str(arg) +")")
#             if arg not in values:
#               values.append(arg)
#         if op == 2:
#             if len(values) > 0:
#                 index = random.randrange(len(values))
#                 arg = values[index]
#             else:
#                 arg = random.randrange(maxnumber) + 1
#             erase(arg)
#             operations.append("erase(" + str(arg)+")")
#             if arg in values:
#               values.remove(arg)

#         if op == 3:
#             prob = random.randrange(2)
#             if prob == 0:
#                 if len(values) > 0:
#                     index = random.randrange(len(values))
#                     arg = values[index]
#                 else:
#                     arg = random.randrange(maxnumber) + 1
#             else:
#                 arg = random.randrange(maxnumber)
#             ret = search(arg)
#             operations.append("search(" + str(arg)+")")
#             if (ret and arg not in values) or (not ret and arg in values):
#                 print("failed search " + str(arg))
#                 print_result(operations)
#                 print(values)
#                 break

#         if op == 4:
#             arg = random.randrange(maxnumber//3)
#             arg2 = random.randrange(arg, maxnumber)
#             test = dosum(arg, arg2)
#             total = sum(x for x in values if x >= arg and x <= arg2)
#             operations.append("test = dosum(" + str(arg) +", " + str(arg2) +")")
#             if test != total:
#                 print("failed sum got-expected", test, total)
#                 print_result(operations)
#                 print(values)
#                 break
#         print("all is going well")
# random_test()
