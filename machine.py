from memory import Tape

class Machine:
    def __init__(self, auxilliary_data, states, transitions, initial_state, initial_tape):
        self.head = 1
        self.auxilliary_data = auxilliary_data  #dictionary of memory names to memory
        self.states = {
            **states,
            'accept': None,
            'halt': None
        } #dictionary of state names to "commands"
        self.transitions = transitions  #dictionary of state name to a symbol
        self.initial_state = initial_state
        self.initial_tape = initial_tape

    def run(self, input_string):
        input_string = '#' + input_string + '#'
        if (init_tape:=self.initial_tape) != '':
            if isinstance(self.auxilliary_data[init_tape], Tape):
                self.auxilliary_data[init_tape].tape = list(input_string)
            else:
                self.auxilliary_data[init_tape].tapes[1] = list(input_string)
        current_state = self.initial_state
        while current:=self.states[current_state]:
            print(current_state)
            if current['state'] == 'S':
                symbol = self.__scan__(input_string)
                transition = (current_state, symbol)
            elif current['state'] == 'SL':
                symbol = self.__scan_left__(input_string)
                transition = (current_state, symbol)
            elif current['state'] == 'P':
                self.__print__(current['to_print'])
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
            current_state = self.transitions.get(transition, 'halt') #invalid transition results to 'halt'
            current_state = current_state[0] if current_state != 'halt' else current_state
        print(current_state)

    def __scan__(self, input_string):
        symbol = input_string[self.head]
        self.head = self.head + 1
        return symbol
    
    def __scan_left__(self, input_string):
        transition = input_string[self.head]
        self.head = self.head - 1
        return transition

    def __read__(self, object_name):
        return self.auxilliary_data[object_name].read()

    def __write__(self, object_name, to_write):
        self.auxilliary_data[object_name].write(to_write)

    def __right__(self, object_name, current_state):
        symbol = self.auxilliary_data[object_name].right()
        transition = (current_state, symbol)
        self.auxilliary_data[object_name].write(self.transitions[transition][1])
        return (current_state, symbol)
    
    def __left__(self, object_name, current_state):
        symbol = self.auxilliary_data[object_name].left()
        transition = (current_state, symbol)
        self.auxilliary_data[object_name].write(self.transitions[transition][1])
        return (current_state, symbol)

    def __up__(self, object_name, current_state):
        symbol = self.auxilliary_data[object_name].up()
        transition = (current_state, symbol)
        self.auxilliary_data[object_name].write(self.transitions[transition][1])
        return (current_state, symbol)

    def __down__(self, object_name, current_state):
        symbol = self.auxilliary_data[object_name].down()
        transition = (current_state, symbol)
        self.auxilliary_data[object_name].write(self.transitions[transition][1])
        return (current_state, symbol)

    def __print__(self, output_string):
        print(output_string)
