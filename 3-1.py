# Implement three stacks using one array
class Stacks:
    def __init__(self, size):
        self.arr = [None for i in range(size)]
        self.tops = [-1, -1, -1]
    
    def add(self, elem, stack):
        aStack = self.arr[:self.tops[stack]+1]
        aStack.append(elem)
        top = len(aStack)-1
        self.tops[stack] = top
        self.arr = aStack + self.arr[self.tops[stack]:]

    def pop(self, stack):
        top = self.tops[stack]
        otherTops = self.tops[:stack] + self.tops[stack+1:]
        if top in otherTops:
            return None


stacks = Stacks(10)
stacks.add(0, 0)
stacks.add(0, 0)
stacks.add(1, 1)
stacks.add(1, 1)
stacks.add(2, 2)
stacks.add(2, 2)
print(stacks.arr, stacks.tops)
stacks.pop(2)
print(stacks.arr, stacks.tops)
stacks.pop(0)
print(stacks.arr, stacks.tops)
