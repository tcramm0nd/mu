
class MU:
    # axiom = 'mi'
    def __init__(self):
        # self.axiom = 'mi'
        self.state = State('mi')
        self.history = History(self.state)

    def __str__(self):
        return str(self.state)

    def __repr__(self):
        return str(self.state)

    def __getitem__(self, item):
        return self.history[item]

    def possible(self):
        '''Displays which rules can be applied to the current string
        '''
        if self.theorem[-1] != 'i':
            self.options[0] = False

        if len(self.theorem) < 1:
            self._ruleII = False

        if 'iii' not in self.theorem:
            self._ruleIII = False

        if 'uu' not in self.theorem:
            self._ruleIV = False

    def ruleI(self):
        '''If you possess a string whose last letter is I, you can add a U at
        the end

        MI -> MIU

        '''
        if self.options[0]:
            self.theorem += 'u'
            self.history.update(self.theorem)
        else:
            print('No can do!')
        self.possible()
    def ruleII(self):
        if self.options[1]:
            self.theorem += self.theorem[1:]
        else:
            print('No can do!')
        self.possible()

    def ruleIII(self, idx):
        if self.options[2]:
            self.theorem = self.theorem[:idx] + 'u' + self.theorem[idx+3:]
        else:
            print('No can do!')
        self.possible()

    def ruleIV(self, idx):
        if self.options[3]:
            self.theorem = self.theorem[:idx] + self.theorem[idx+2:]
        else:
            print('No can do!')
        self.possible()


class State:
    """
    The current state of the game, including the current string, and the available options
    """

    def __init__(self, string):
        super(State, self).__init__()
        self.string = string
        self.options = [True, True, True, True]
        if self.string[-1] != 'i':
            self.options[0] = False

        if len(self.string) < 1:
            self.options[1] = False

        if 'iii' not in self.string:
            self.options[2] = False

        if 'uu' not in self.string:
            self.options[3] = False

    # def __getitem__(self, item):
    #     return self.string, self.options

    def __str__(self):
        return f'Current String: {self.string}\nCurrent Options: {self.options}'




class History(State):
    '''Displays the history of the string and the rules used to get to that
    state'''
    def __init__(self, state):
        super(State, self).__init__()
        self.strings = [state.string]
        self.options = [state.options]
        # self.options_hist = []
        # self.options_hist.append(state[1])

    def __str__(self):
        return str(self.string)

    def __repr__(self):
        return str(self.state)

    def __getitem__(self, item):
        return self.strings[item], self.options[item]

    def update(self, string, options):
        self.strings.insert(0, theorem)
        self.options.insert(0, options)

    def load(self):
        '''Loads a certain historical state'''
    def undo(self):
        '''reverts to the previous state'''
