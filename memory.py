class Stack:
    def __init__(self):
        self.memory = []

    def read(self):
        return self.memory.pop()

    def write(self, to_write):
        self.memory.append(to_write)

class Queue:
    def __init__(self):
        self.memory = []

    def read(self):
        return self.memory.pop(0)
    
    def write(self, to_write):
        self.memory.append(to_write)

class Tape:
    def __init__(self):
        self.memory = ['#']
        self.tape_head = 0

    def right(self):
        if len(tape:=self.memory) == (tape_head:=(self.tape_head + 1)):
            tape.append('#')
        symbol = tape[tape_head]
        self.tape_head = tape_head
        return symbol

    def left(self): #greatly assumes that it is impos   sible to go infinitely left
        symbol = self.memory[tape_head:=(self.tape_head - 1)]
        self.tape_head = tape_head
        return symbol

    def write(self, to_write):
        self.memory[self.tape_head] = to_write

class Tape2D:
    def __init__(self):
        self.memory = [['#'], ['#']]
        self.x_head = 0
        self.y_head = 1

    def right(self):
        if len(tape:=self.memory[self.y_head]) == (x_head:=(self.x_head + 1)):
            tape.append('#')
        symbol = tape[x_head]
        self.x_head = x_head
        return symbol
    
    def left(self): #greatly assumes that it is impossible to go infinitely left
        symbol = self.memory[self.y_head][x_head:=self.x_head - 1]
        self.x_head = x_head
        return symbol

    def down(self):
        if (length:=len(tapes:=self.memory)) == (y_head:=(self.y_head + 1)):
            tapes.append(['#'] * length)
        if x_length:=len(tape:=tapes[y_head]) <= (x_head:=(self.x_head)):
            tape.append(['#'] * (x_head - x_length + 1))
        symbol = tapes[y_head][x_head]
        self.y_head = y_head
        return symbol

    def up(self): #greatly assumes that it is impossible to go infinitely up
        symbol = self.memory[y_head:=self.y_head - 1][self.x_head]
        self.y_head = y_head
        return symbol
    
    def write(self, to_write):
        self.memory[self.y_head][self.x_head] = to_write