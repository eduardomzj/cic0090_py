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


class Fila_comPilhas:

    def __init__(self):
        self.pilha1 = Stack()
        self.pilha2 = Stack()

    def enqueue(self, item):
        self.pilha1.push(item)

    def dequeue(self):

        if self.pilha1.isEmpty() and self.pilha2.isEmpty():
            return None
        
        if self.pilha2.isEmpty():
            while not self.pilha1.isEmpty():
                self.pilha2.push(self.pilha1.pop())
        return self.pilha2.pop()
    
def imprime(self):
    aux = Stack()

    while not self.pilha2.isEmpty():
        item = self.pilha2.pop()
        print(item)
        aux.push(item)

    while not aux.isEmpty():
        self.pilha2.push(aux.pop())

    while not self.pilha1.isEmpty():
        aux.push(self.pilha1.pop())

    while not aux.isEmpty():
        item = aux.pop()
        print(item)
        self.pilha1.push(item)
    

