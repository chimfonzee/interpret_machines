import re

create_data = False
current = None
auxilliary_data = {}
state_diagram = {'accept': None, 'halt': None}
commands = []
head = 1

input_string = '#01010101#'

class BaseState:
    def __init__(self, transitions):
        self.transitions = transitions

    def action(self, head):
        print(f'action() is not yet overriden head: {head}')


class ScanLeftState(BaseState):
    def action(self, head):
        transition = input_string[head]
        return head - 1, self.transitions[transition]


class ScanState(BaseState):
    def action(self, head):
        transition = input_string[head]
        return head + 1, self.transitions[transition]


class PrintState(BaseState):
    def action(self, head):
        to_print = self.transitions.keys[0]
        print(to_print)
        return head, self.transitions[to_print]


# class 

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


with open('scan_test.txt') as input:
    for lines in input.readlines():
        line = lines.rstrip()
        tokens = line.split(' ')
        new_state = None

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
                if (ext:=tokens[2]) == 'LEFT':
                    transitions = {}

                    for (symbol, target) in re.findall(r'(\w|#),(\w+)', line):
                        if transition:=transitions.get(symbol, None):
                            transition.append(target)
                        else:
                            transitions[symbol] = [target]

                    new_state = ScanLeftState(transitions)
                else: #RIGHT
                    transitions = {}

                    for (symbol, target) in re.findall(r'(\w|#),(\w+)', line):
                        if transitions.get(symbol, None):
                            transitions[symbol].append(target)
                        else:
                            transitions[symbol] = [target]

                    new_state = ScanState(transitions)
            elif command == 'PRINT':
                transitions = {}

                for (symbol, target) in re.findall(r'(\w|#),(\w+)', line):
                    if transition:=transitions.get(symbol, None):
                        transition.append(target)
                    else:
                        transitions[symbol] = [target]

                new_state = PrintState(transitions)
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

            state_diagram[state.split(']', 1)[0]] = new_state
            current = current if current else new_state

def traverse(head, state, halt):
    if halt or not state:
        return True

    new_head, transitions = state.action(head)

    for transition in transitions:
        halt = traverse(new_head, state_diagram[transition], halt)


traverse(head, current, False)

#check how to create multiple state objects (aka data)