from memory import Stack, Queue, Tape, Tape2D

class Machine:
    def update(self, auxilliary_data, states, transitions, initial_state, initial_tape):
        self.auxilliary_data = auxilliary_data  #dictionary of memory names to memory
        self.states = {
            **states,
            'accept': None,
            'reject': None,
            'halt': None
        } #dictionary of state names to "commands"
        self.transitions = transitions  #dictionary of state name to a symbol
        self.initial_state = initial_state
        self.initial_tape = initial_tape

    def add_websocket(self, websocket):
        self.websocket = websocket

    def __prepare__(self):
        auxilliary_data = {}
        for key in self.auxilliary_data:
            memory = self.auxilliary_data[key]
            if memory == 'STACK':
                auxilliary_data[key] = Stack()
            elif memory == 'QUEUE':
                auxilliary_data[key] = Queue()
            elif memory == 'TAPE':
                auxilliary_data[key] = Tape()
            else:
                auxilliary_data[key] = Tape2D()
        self.current_data = auxilliary_data
        self.head = 1

    async def run(self, input_string, run):
        to_return = ''
        self.__prepare__()
        if (init_tape:=self.initial_tape) != '':
            print()
            if isinstance(self.current_data[init_tape], Tape):
                self.current_data[init_tape].memory = list(input_string)
            else:
                self.current_data[init_tape].memory[1] = list(input_string)
        current_state = self.initial_state
        while current:=self.states[current_state]:
            await self.websocket.send_json({
                'current_state': current_state,
                'memory': {memory_object: vars(memory) for (memory_object, memory) in self.current_data.items()},
                'tape_head': self.head,
                'run': run
            })
            # print(current_state)
            try:
                if current['state'] == 'S':
                    symbol = self.__scan__(input_string)
                    transition = (current_state, symbol)
                elif current['state'] == 'SL':
                    symbol = self.__scan_left__(input_string)
                    transition = (current_state, symbol)
                elif current['state'] == 'P':
                    to_return = to_return + current['to_print']
                    transition = (current_state, current['to_print'])
                elif current['state'] == 'R':
                    symbol = self.__read__(current['object_name'])
                    transition = (current_state, symbol)
                elif current['state'] == 'W':
                    self.__write__(current['object_name'], symbol:=current['to_write'])
                    transition = (current_state, symbol)
                elif current['state'] == 'TR':
                    transition = self.__right__(current['object_name'], current_state)
                elif current['state'] == 'TL':
                    transition = self.__left__(current['object_name'], current_state)
                elif current['state'] == 'TU':
                    transition = self.__up__(current['object_name'], current_state)
                elif current['state'] == 'TD':
                    transition = self.__down__(current['object_name'], current_state)
                current_state = self.transitions.get(transition, 'reject') #invalid transition results to 'reject'
                if not current_state in ['reject', 'halt', 'accept']:
                    current_state = current_state[0]
            except Exception as e:
                print(e)
                current_state = 'reject'
        await self.websocket.send_json({
            'current_state': current_state,
            'memory': {memory_object: vars(memory) for (memory_object, memory) in self.current_data.items()},
            'tape_head': self.head,
            'run': run
        })
        return to_return

    def __scan__(self, input_string):
        self.head = self.head + 1
        symbol = input_string[self.head]
        return symbol
    
    def __scan_left__(self, input_string):
        self.head = self.head - 1
        transition = input_string[self.head]
        return transition

    def __read__(self, object_name):
        return self.current_data[object_name].read()

    def __write__(self, object_name, to_write):
        self.current_data[object_name].write(to_write)

    def __right__(self, object_name, current_state):
        symbol = self.current_data[object_name].right()
        transition = (current_state, symbol)
        self.current_data[object_name].write(self.transitions[transition][1])
        return (current_state, symbol)
    
    def __left__(self, object_name, current_state):
        symbol = self.current_data[object_name].left()
        transition = (current_state, symbol)
        self.current_data[object_name].write(self.transitions[transition][1])
        return (current_state, symbol)

    def __up__(self, object_name, current_state):
        symbol = self.current_data[object_name].up()
        transition = (current_state, symbol)
        self.current_data[object_name].write(self.transitions[transition][1])
        return (current_state, symbol)

    def __down__(self, object_name, current_state):
        symbol = self.current_data[object_name].down()
        transition = (current_state, symbol)
        self.current_data[object_name].write(self.transitions[transition][1])
        return (current_state, symbol)

    # def __print__(self, output_string):
    #     print(output_string)
