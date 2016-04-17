# python3

import sys, threading
sys.setrecursionlimit(10**8) # max depth of recursion
threading.stack_size(2**32)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())
                self.parent = list(map(int, sys.stdin.readline().split()))

                self.children = {}
                for index, element in enumerate(self.parent):
                    if element not in self.children:
                        self.children[element] = [index]
                    else:
                        self.children[element].append(index)

        def get_children(self, element_index):
            if element_index not in self.children:
                print("Setting children for " + str(element_index))
                self.children[element_index] = [index for index, el in enumerate(self.parent) if el == element_index]
            return self.children[element_index]

        def compute_height(self):
                root_index = self.parent.index(-1)
                return(self.height(root_index) + 1)

        def height(self, index):
            children_heights = [self.height(index) for index in self.children.get(index, [])]
            if len(children_heights) == 0:
                return 0
            return 1 + max(children_heights)

def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
