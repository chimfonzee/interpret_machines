class Stack:
    def __init__(self):
        self.stack = []

    def read(self):
        return self.stack.pop()

    def write(self, to_write):
        self.stack.append(to_write)

class Queue:
    def __init__(self):
        self.queue = []

    def read(self):
        return self.queue.pop(0)
    
    def write(self, to_write):
        self.queue.append(to_write)

class Tape:
    def __init__(self):
        self.tape = ['#']
        self.tape_head = 0

    def right(self):
        if len(tape:=self.tape) == (tape_head:=(self.tape_head + 1)):
            tape.append('#')
        symbol = tape[tape_head]
        self.tape_head = tape_head
        return symbol

    def left(self): #greatly assumes that it is impossible to go infinitely left
        symbol = self.tape[tape_head:=(self.tape_head - 1)]
        self.tape_head = tape_head
        return symbol

    def write(self, to_write):
        self.tape[self.tape_head] = to_write

class Tape2D:
    def __init__(self):
        self.tapes = [['#'], ['#']]
        self.x_head = 0
        self.y_head = 0

    def right(self):
        if len(tape:=self.tapes[self.y_head]) == (x_head:=(self.x_head + 1)):
            tape.append('#')
        symbol = tape[x_head]
        self.x_head = x_head
        return symbol
    
    def left(self): #greatly assumes that it is impossible to go infinitely left
        symbol = self.tapes[self.y_head][x_head:=self.x_head - 1]
        self.x_head = x_head
        return symbol

    def right(self):
        if length:=len(tapes:=self.tapes) == (y_head:=(self.y_head + 1)):
            tapes.append(['#'] ** length)
        if x_length:=len(tape:=tapes[y_head]) <= (x_head:=(self.x_head)):
            tape.append(['#'] ** (x_head - x_length + 1))
        symbol = tapes[y_head][x_head]
        self.y_head = y_head
        return symbol

    def up(self): #greatly assumes that it is impossible to go infinitely up
        symbol = self.tapes[y_head:=self.y_head - 1][self.x_head]
        self.y_head = y_head
        return symbol