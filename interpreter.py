create_data = False
auxilliary_data = {}
state_diagram = {}
commands = []

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
        self.tape = []

    def right(self):
        pass

    def write(self):
        pass

class Tape2D:
    def __init__(self):
        self.tapes = []

with open('input.txt') as input:
    for lines in input.readlines():
        tokens = lines.rstrip().split(' ')

        if (state:=tokens[0]) == '.DATA':
            create_data = True
        elif state == '.LOGIC':
            create_data = False
        elif create_data:
            if state == 'STACK':
                auxilliary_data[tokens[1]] = Stack()
            elif state == 'QUEUE':
                auxilliary_data[tokens[1]] = Queue()
            elif state == 'TAPE':
                auxilliary_data[tokens[1]] = Tape()
            elif state == '2D_TAPE':
                auxilliary_data[tokens[1]] = Tape2D()
        elif not create_data:
            if (command:=tokens[1]) == 'SCAN':
                commands.append(command)
            elif command == 'PRINT':
                commands.append(command)
            elif (command:=command.split('(', 1)[0].strip()) == 'READ':
                commands.append(command)
            elif command == 'WRITE':
                commands.append(command)
            elif command == 'RIGHT':
                commands.append(command)
            elif command == 'LEFT':
                commands.append(command)
            elif command == 'UP':
                commands.append(command)
            elif command == 'DOWN':
                commands.append(command)

print(commands)
print(auxilliary_data)