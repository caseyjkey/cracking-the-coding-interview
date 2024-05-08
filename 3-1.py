# Implement three stacks using one array
class Stacks:
    def __init__(self, size):
        self.arr = [None for i in range(size)]
        self.tops = [-1, -1, -1]
    
    def add(self, elem, stack):
        if stack == 0:
            self.tops[0] += 1
        elif stack == 1:
            if self.tops[1] == -1:
                mid = len(self.arr) // 2
                self.tops[1] = mid
            else:
                self.tops[1] += 1
        else:
            if self.tops[2] == -1:
                self.tops[2] = len(self.arr)
            self.tops[2] -= 1
        self.arr[self.tops[stack]] = elem


    def pop(self, stack):
        top = self.tops[stack]
        elem = self.arr[top]
        self.arr[top] = None
        if stack == 0 or stack == 1:
            self.tops[stack] -= 1
        else:
            self.tops[2] += 1
        return elem
                    

stacks = Stacks(10)
stacks.add(0, 0)
stacks.add(0, 0)
stacks.add(1, 1)
stacks.add(1, 1)
stacks.add(2, 2)
stacks.add(2, 2)
print(stacks.arr, stacks.tops)
print('pop', stacks.pop(2))
print(stacks.arr, stacks.tops)
print(stacks.pop(0))
print(stacks.arr, stacks.tops)
