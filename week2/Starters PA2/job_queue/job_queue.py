# python3

class CustomHeapSort:
  def __init__(self, data = [], key=None, arity=2):
    self.data = data
    self.key = key
    self.tree_size = len(data)
    self.arity = arity

  def parent(self, i):
    return (i - 1) // 2

  def children(self, i):
    return range((i - 1) * self.arity + 3, min(self.tree_size, (i - 1)*self.arity + self.arity + 3))

  def sift_up(self, i):
    while i > 0 and self.parent_value(i) > self.value_at(i):
      self.swap(self.parent(i), i)
      i = self.parent(i)

  def sift_down(self, i):
    min_index = i
    for child in self.children(i):
      if child < self.tree_size:
        if ((self.value_at(child) == self.value_at(min_index)) and (self.data[child][0] < self.data[min_index][0])):
          min_index = child
        if (self.value_at(child) < self.value_at(min_index)):
          min_index = child

    if i != min_index:
      self.swap(i, min_index)
      self.sift_down(min_index)

  def insert(self, el):
    if len(self.data) == self.tree_size:
      self.data.append(el)
    else:
      self.data[self.tree_size] = el
    self.tree_size += 1
    self.sift_up(self.tree_size - 1)

  def extract(self):
    max_element = self.data[0]
    self.swap(0, self.tree_size - 1)
    self.tree_size -= 1
    self.sift_down(0)
    return max_element

  def swap(self, i, j):
    self.data[i], self.data[j] = self.data[j], self.data[i]

  def parent_value(self, i):
    return self.value_at(self.parent(i))

  def value_at(self, i):
    if self.key != None:
      return self.data[i][self.key]
    else:
      return self.data[i]

  def tree(self):
    return self.data[:self.tree_size]

  def build_heap(self, array):
    self.data = array
    self.tree_size = len(array)
    for i in range((self.tree_size - 1)//2, -1, -1):
      self.sift_down(i)


class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i])

    def assign_jobs(self):
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        sorter = CustomHeapSort(key = 1)
        for worker in range(self.num_workers):
          sorter.insert((worker, 0))
        for i in range(len(self.jobs)):
          self.assigned_workers[i], self.start_times[i] = sorter.extract()
          sorter.insert((self.assigned_workers[i], self.start_times[i] + self.jobs[i]))

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
