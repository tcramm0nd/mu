
class MU:
    def __init__(self):
        self.axiom = 'mi'
        self.theorem = self.axiom
        self.history = ['mi']


    def __str__(self):
        print(self.theorem.upper())

    def __getitem__(self, item):
        return [self.history[item]]

    def options(self):
        '''Displays which rules can be applied to the current string
        '''
        if self.theorem[-1] != 'i':
            self.ruleI = False

        if len(self.theorem < 1):
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
        assert self.theorem.endswith('i'), f"The String {self.theorem} does not \
                                                end with 'I'"

        self.theorem += 'u'
        return self.theorem

    def ruleII(self):

        self.theorem += self.theorem[1:]
        return self.theorem

    def ruleIII(self, idx):

        self.theorem = self.theorem[:idx] + 'u' + self.theorem[idx+3:]
        return self.theorem

    def ruleIV(sel, idx):

        self.theorem = self.theorem[:idx] + self.theorem[idx+2:]
        return self.theorem

class History(MU):
    '''Displays the history of the string and the rules used to get to that
    state'''

    def load(self):
        '''Loads a certain historical state'''
    def undo(self):
        '''reverts to the previous state'''
