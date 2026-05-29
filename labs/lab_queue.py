class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.isEmpty():
            return
        return self.items.pop()

    def peek(self):
        if self.isEmpty():
            return
        return self.items[-1]

    def size(self):
        return len(self.items)
    
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        if self.isEmpty():
            return
        return self.items.pop()

    def size(self):
        return len(self.items)

    def print(self):
        for i in range(self.size()):
            print(f"{self.items[self.size()-i-1]}", end=", ")

class Caferia:
    def __init__(self):
        self.alunos = Queue()
        self.lanches = Stack()

def serve_almoco(self):

    recusas = 0

    while not self.alunos.isEmpty() and not self.lanches.isEmpty():
        aluno = self.alunos.dequeue()
        sanduiche = self.lanches.peek()

        if aluno == sanduiche:
            self.sanduiche.pop()
            recusas = 0
        else:
            self.alunos.enqueue(aluno)
            recusas += 1
        
        if recusas == self.alunos.size():
            break

        print(self.alunos.size())
    
