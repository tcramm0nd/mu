
class MU:
    def __init__(self):
        self.axiom = 'mi'
        self.theorem = self.axiom
        self.options = [self.ruleI, self.ruleII, self.ruleIII, self.ruleIV]
        self.state = [self.theorem, self.options]
        self.history = [self.state]

    def __str__(self):
        return self.theorem.upper()
    def __repr__(self):
        return self.theorem.upper()

    def __getitem__(self, item):
        return [self.history[item]]

    def possible(self):
        '''Displays which rules can be applied to the current string
        '''
        if self.theorem[-1] != 'i':
            self.ruleI = False

        if len(self.theorem) < 1:
            self.ruleII = False

        if 'iii' not in self.theorem:
            self.ruleIII = False

        if 'uu' not in self.theorem:
            self.ruleIV = False

    def load(self):
        '''Loads a certain historical state'''
    def undo(self):
        '''reverts to the previous state'''


    def ruleI(self):
        '''If you possess a string whose last letter is I, you can add a U at
        the end

        MI -> MIU

        '''
        if self.options[0]:
            self.theorem += 'u'
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

    def ruleIV(sel, idx):
        if self.options[3]:
            self.theorem = self.theorem[:idx] + self.theorem[idx+2:]
        else:
            print('No can do!')
        self.possible()

class History(MU):
    '''Displays the history of the string and the rules used to get to that
    state'''
    def __init__(self):
        self.h = MU.axiom
    def load(self):
        '''Loads a certain historical state'''
    def undo(self):
        '''reverts to the previous state'''
