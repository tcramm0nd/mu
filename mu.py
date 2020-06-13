
class MU:
    # axiom = 'mi'
    def __init__(self):
        self.axiom = 'mi'
        self.theorem = self.axiom
        self.options = {'ruleI':True,
                        'ruleII':True,
                        'ruleIII': False,
                        'ruleIV': False}
        self.history = [self.axiom, self.options]
        self.current_state = self.history[-1]

    def __str__(self):
        return str(self.theorem)

    def __repr__(self):
        return str(self.state)

    def __getitem__(self, item):
        return self.history[item]

    def possible(self):
        '''
        Updates which rules can be applied to the current string
        '''
        if self.theorem[-1] != 'i':
            self.options['ruleI'] = False

        if len(self.theorem) < 1:
            self.options['ruleII'] = False

        if 'iii' not in self.theorem:
            self.options['ruleIII'] = False

        if 'uu' not in self.theorem:
            self.options['ruleIV'] = False

    def ruleI(self):
        '''If you possess a string whose last letter is I, you can add a U at
        the end

        MI -> MIU

        '''
        if self.options['ruleI']:
            self.theorem += 'u'
            self.update()

        else:
            print('No can do!')
        # self.possible()
    def ruleII(self):
        if self.options['ruleII']:
            self.theorem += self.theorem[1:]
        else:
            print('No can do!')
        self.possible()

    def ruleIII(self, idx):
        if self.options['ruleIII']:
            self.theorem = self.theorem[:idx] + 'u' + self.theorem[idx+3:]
        else:
            print('No can do!')
        self.possible()

    def ruleIV(self, idx):
        if self.options['ruleIV']:
            self.theorem = self.theorem[:idx] + self.theorem[idx+2:]
        else:
            print('No can do!')
        self.possible()

    def update(self):
        self.possible()
        self.history.append(self.current_state)
# class History:
#     """
#     The current state of the game, including the current string, and the available options
#     """
#
#     def __init__(self, string, options=None):
#         super(History, self).__init__()
#         self.string = string
#
#         if options:
#             self.options =  options
#         else:
#             self.options = {'RuleI': False,
#                             'RuleII': False,
#                             'RuleIII': False,
#                             'RuleIV': False}
#             if self.string[-1] == 'i':
#                 self.options['RuleI'] = True
#
#             if len(self.string) > 1:
#                 self.options['RuleII'] = True
#
#             if 'iii' in self.string:
#                 self.options['RuleIII'] = True
#
#             if 'uu' in self.string:
#                 self.options['RuleIV'] = False
#
#
#     def __str__(self):
#         return f'Current String: {self.string}\nCurrent Options: {self.options}'
#
#     def __repr__(self):
#         return str(self.string)
#
#     def __getitem__(self, item):
#         return self.string[item], self.options[item]
#

#
#     def load(self):
#         '''Loads a certain historical state'''
#     def undo(self):
#         '''reverts to the previous state'''
