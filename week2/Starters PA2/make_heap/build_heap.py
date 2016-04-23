# python3
class HeapSort:
  def __init__(self, data = []):
    self.data = data
    self.tree_size = len(data)
    self.swaps = []

  def parent(self, i):
    return (i - 1) // 2

  def left_child(self, i):
    return 2 * i + 1

  def right_child(self, i):
    return 2 * i + 2

  def sift_up(self, i):
    while i > 0 and self.parent_value(i) > self.data[i]:
      self.swap(self.parent(i), i)
      i = self.parent(i)

  def sift_down(self, i):
    min_index = i
    l = self.left_child(i)
    if l <= self.tree_size - 1 and self.data[l] < self.data[min_index]:
      min_index = l

    r = self.right_child(i)
    if r <= self.tree_size - 1 and self.data[r] < self.data[min_index]:
      min_index = r

    if i != min_index:
      self.swap(i, min_index)
      self.sift_down(min_index)

  def swap(self, i, j):
    self.swaps.append([i, j])
    self.data[i], self.data[j] = self.data[j], self.data[i]

  def insert(self, el):
    self.data.append(el)
    self.tree_size += 1
    self.sift_up(len(self.data) - 1)

  def extract_max(self):
    max_element = self.data[0]
    self.swap(0, self.tree_size - 1)
    self.tree_size -= 1
    self.sift_down(0)
    return max_element

  def parent_value(self, i):
    return self.data[self.parent(i)]

  def build_heap(self, array):
    self.data = array
    self.tree_size = len(array)
    for i in range((self.tree_size - 1)//2, -1, -1):
      self.sift_down(i)


class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []

  def ReadData(self):
    n = int(input())
    self._data = [int(s) for s in input().split()]
    assert n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self):
    # The following naive implementation just sorts
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap,
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    # for i in range(len(self._data)):
    #   for j in range(i + 1, len(self._data)):
    #     if self._data[i] > self._data[j]:
    #       self._swaps.append((i, j))
    #       self._data[i], self._data[j] = self._data[j], self._data[i]
    sorter = HeapSort()
    sorter.build_heap(self._data)
    self._swaps = sorter.swaps

  def Solve(self):
    self.ReadData()
    self.GenerateSwaps()
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
