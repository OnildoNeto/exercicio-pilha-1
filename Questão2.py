class Pilha:
    def __init__ (self):
        self.items = []

    def isVazio (self):
        return self.items == 0

    def push (self, item):
        if item in self.items:
            pilha = list(set(pilha))

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def lenght(self):
        return len(self.items)
        
pilha = Pilha()
