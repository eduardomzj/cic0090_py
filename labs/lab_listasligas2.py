class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def imprimir(self):
        atual = self.head
        s = ""

        while atual != None:
            s = s + " " + str(atual.getData())
            atual = atual.getNext()

        print(s[1:])

    def addInicio(self, item):
        novo = Node(item)
        novo.setNext(self.head)
        self.head = novo

    def buscar(self, item):
        atual = self.head
        anterior = None

        while atual != None:
            if atual.getData() == item:

                if anterior == None:
                    return item

                anterior.setNext(atual.getNext())

                atual.setNext(self.head)
                self.head = atual

                return item

            anterior = atual
            atual = atual.getNext()

        return None