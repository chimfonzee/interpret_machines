import re

from memory import Stack, Queue, Tape, Tape2D
from machine import Machine

auxilliary_data = {}
transitions = {}
states = {}
current = ''
initial_tape = ''

with open('model.txt') as input:
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
                if initial_tape == '':
                    initial_tape = tokens[1]
                auxilliary_data[tokens[1]] = Tape()
            elif state == '2D_TAPE':
                # if initial_tape == '':
                #     initial_tape = tokens[1]
                auxilliary_data[tokens[1]] = Tape2D()
        elif not create_data:
            state = {}

            if (command:=tokens[1]) == 'SCAN':
                if (ext:=tokens[2]) == 'LEFT':
                    for (symbol, target) in re.findall(r'(\w|#),(\w+)', line):
                        transitions[(tokens[0][:-1], symbol)] = (target)
                    state = {'state': 'SL'}
                else: #RIGHT
                    for (symbol, target) in re.findall(r'(\w|#),(\w+)', line):
                        transitions[(tokens[0][:-1], symbol)] = (target)
                    state = {'state': 'S'}
            elif command == 'PRINT':
                for (symbol, target) in re.findall(r'(\w|#),(\w+)', line):
                    transitions[(tokens[0][:-1], symbol)] = (target)

                state = {
                    'state': 'P',
                    'to_print': symbol
                }
            elif (token_command:=command.split('(', 1)[0].strip()) == 'READ':
                for (symbol, target) in re.findall(r'(\w|#),(\w+)', line):
                    transitions[(tokens[0][:-1], symbol)] = (target)
                
                state = {
                    'state': 'R',
                    'object_name': re.search(r'\((\w+)\)', command)[0][1:-1]
                }
            elif token_command == 'WRITE':
                for (symbol, target) in re.findall(r'(\w|#),(\w+)', line):
                    transitions[(tokens[0][:-1], symbol)] = (target)

                state = {
                    'state': 'W',
                    'object_name': re.search(r'\((\w+)\)', command)[0][1:-1],
                    'to_write': symbol
                }
            elif token_command == 'RIGHT':
                for (symbol, to_write, target) in re.findall(r'(\w|#)/(\w|#),(\w+)', line):
                    transitions[(tokens[0][:-1], symbol)] = (target, to_write)

                state = {
                    'state': 'TR',
                    'object_name': re.search(r'\((\w+)\)', command)[0][1:-1]
                }
            elif token_command == 'LEFT':
                for (symbol, to_write, target) in re.findall(r'(\w|#)/(\w|#),(\w+)', line):
                    transitions[(tokens[0][:-1], symbol)] = (target, to_write)

                state = {
                    'state': 'TL',
                    'object_name': re.search(r'\((\w+)\)', command)[0][1:-1]
                }
            elif token_command == 'UP':
                for (symbol, to_write, target) in re.findall(r'(\w|#)/(\w|#),(\w+)', line):
                    transitions[(tokens[0][:-1], symbol)] = (target, to_write)

                state = {
                    'state': 'TU',
                    'object_name': re.search(r'\((\w+)\)', command)[0][1:-1]
                }
            elif token_command == 'DOWN':
                for (symbol, to_write, target) in re.findall(r'(\w|#)/(\w|#),(\w+)', line):
                    transitions[(tokens[0][:-1], symbol)] = (target, to_write)

                state = {
                    'state': 'TD',
                    'object_name': re.search(r'\((\w+)\)', command)[0][1:-1]
                }
            states[tokens[0][:-1]] = state
            current = current if current != '' else tokens[0][:-1]

sample_machine = Machine(auxilliary_data, states, transitions, current, initial_tape)
print(sample_machine)
print(sample_machine.auxilliary_data)
print(sample_machine.initial_state)
print(sample_machine.head)
print(sample_machine.initial_tape)
print(sample_machine.states)
print(sample_machine.transitions)
with open('input.txt') as input:
    to_run = input.readline().strip()
    sample_machine.run(to_run)