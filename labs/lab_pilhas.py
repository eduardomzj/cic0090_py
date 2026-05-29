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


N = int(input()) 
for _ in range(N):
    expressao = input()

    pilha_parenteses = Stack()
    pilha_colchete = Stack()
    pilha_chave = Stack()

    verificador = False

    for n in expressao:
        if n!= ')':
            pilha_parenteses.push(n)
        else:
            topo = pilha_parenteses.peek()

            if topo == '(':
                verificador = True
                break
            else:
                while pilha_parenteses.peek() != '(':
                    pilha_parenteses.pop()

            pilha_parenteses.pop()

    for n in expressao:
        if n!= ']':
            pilha_colchete.push(n)
        else:
            topo = pilha_colchete.peek()

            if topo == '[':
                verificador = True
                break
            else:
                while pilha_colchete.peek() != '[':
                    pilha_colchete.pop()
                    
            pilha_colchete.pop()
    
    for n in expressao:
        if n!= '}':
            pilha_chave.push(n)
        else:
            topo = pilha_chave.peek()

            if topo == '{':
                verificador = True
                break
            else:
                while pilha_chave.peek() != '{':
                    pilha_chave.pop()
                    
            pilha_chave.pop()

    if verificador is True:
        print('A expressão possui duplicata.')
    else:
        print('A expressão não possui duplicata.')
    
