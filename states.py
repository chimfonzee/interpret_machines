class BaseState:
    def __init__(self, transitions):
        self.transitions = transitions


class ScanLeftState(BaseState):
    def action(self):
        global head

        transition = input_string[head]
        head = head - 1
        return self.transitions[transition]

class ScanState(BaseState):
    def action(self):
        global head

        transition = input_string[head]
        head = head + 1
        return self.transitions[transition]


class PrintState(BaseState):
    def action(self, to_print):
        print(to_print)
        return self.transitions[to_print]