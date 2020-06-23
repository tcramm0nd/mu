import os
import csv

class MU:
    def __init__(self):
        self.axiom = 'mi'
        self.theorem = self.axiom
        self.start_options = [True,
                              True,
                              False,
                              False]
        self.history = []
        self.redo_history = []

        self.history.append([self.axiom, self.start_options])
        self.options = self.history[-1][1]

        self.rule_list = ['Rule I',
                          'Rule II',
                          'Rule III',
                          'Rule IV']
        self.rules = Rules()

        self.save_data = 'saved_games/'

    def __str__(self):
        # display = ' '.join(self.history)
        display = ''
        for l in self.history:
            string = f'String: {l[0]}\n'
            opts = l[1]
            rI = f'RuleI: {opts[0]}\n'
            rII = f'RuleII: {opts[1]}\n'
            rIII = f'RuleIII: {opts[2]}\n'
            rIV = f'RuleIV: {opts[3]}\n'



            display += string + rI + rII + rIII + rIV + '\n'
        # return str(self.history)
        return display

    def __repr__(self):
        return str(self.history)

    def __getitem__(self, item):
        return self.history[item]


    def execute_rule(self, player_input):
        if player_input in self.rules.I:
            self.ruleI()
        elif player_input in self.rules.II:
            self.ruleII()
        elif player_input in self.rules.III:
            idx = self.idx(player_input)
            self.ruleIII(idx)
        elif player_input in self.rules.IV:
            idx = self.idx(player_input)
            self.ruleIV(idx)
        else:
            print('No can do')
            return

    def idx(self, player_input):
        '''
        Gets te index to operate ruleIII and RuleIV
        '''
        string = []
        idx = []
        for i, c in enumerate(self.theorem):
            string.append(c)
            idx.append(str(i + 1))

        idx_string = ' '.join(string)
        indices = ' '.join(idx)

        print(idx_string)
        print(indices)

        idx_input = int(input(
            f'Enter the location you would like to execute {player_input}: ')) - 1

        return idx_input

    def ruleI(self):
        if self.options[0]:
            self.theorem += 'u'
            self.update()
        else:
            print('No can do!')

    def ruleII(self):
        if self.options[1]:
            self.theorem += self.theorem[1:]
            self.update()
        else:
            print('No can do!')

    def ruleIII(self, idx):
        if self.options[2] and self.theorem[idx:idx+3] == 'iii':
            self.theorem = self.theorem[:idx] + 'u' + self.theorem[idx+3:]
            self.update()
        else:
            print('No can do!')

    def ruleIV(self, idx):
        if self.options[3] and self.theorem[idx:idx+2] == 'uu':
            self.theorem = self.theorem[:idx] + self.theorem[idx+2:]
            self.update()
        else:
            print('No can do!')

    def update(self):
        options = self.possible()
        state = [self.theorem, options]
        self.history.append(state)
        self.options = self.history[-1][1]

        if self.options[0]==False and self.options[1]==False and self.options[2]==False and self.options[3]==False:
            self.lose = True

        print(f'New String: {self.theorem}')
        for i, o in enumerate(self.options):
            print(f'{self.rule_list[i]}: {o}')

    def possible(self):
        '''
        Updates which rules can be applied to the current string

        trying to return a dict, otherwise switch options to a list maybe
        '''
        options = [None] * 4
        if self.theorem[-1] == 'i':
            options[0] = True
        else:
            options[0] = False

        if len(self.theorem) > 1:
            options[1] = True
        else:
            options[1] = False

        if 'iii' in self.theorem:
            options[2] = True
        else:
            options[2] = False

        if 'uu' in self.theorem:
            options[3] = True
        else:
            options[3] = False

        return options

    def undo(self):
        if len(self.history) > 1:
            self.redo_history.append(self.history.pop())
            self.theorem = self.history[-1][0]
            self.options = self.history[-1][1]

            print(f'New String:{self.theorem}')
            for i, o in enumerate(self.options):
                print(f'{self.rule_list[i]}: {o}')
        else:
            print('Nothing to Undo!')
            # return
    def redo(self):
        if len(self.history) >= 1 and len(self.redo_history) >= 1:
            self.history.append(self.redo_history.pop())
            self.theorem = self.history[-1][0]
            self.options = self.history[-1][1]
            print('new')
            print(self.theorem)
            print(self.options)
        else:
            print('Nothing to Redo!')
            return

    def save(self):
        if os.path.isdir(self.save_data) != True:
            os.mkdir(self.save_data)

        #join file name and dir
        #join file name and '.csv'

        file_name = input('file name') + '.csv'
        file = os.path.join(self.save_data, file_name)

        with open(file, 'w') as f:
            f_csv = csv.writer(f)
            f_csv.writerows(self.history)

    def load(self):
        if os.path.isdir(self.save_data) != True:
            print('No Saved Games Found!')

        #join file name and dir

        file_name = input('file name')

        self.history = []
        self._history = []

        with open('test.csv') as f:
            f_csv = csv.reader(f)
            for row in f_csv:
                self._history.append(row)

        for line in self._history:
            string = line[0]
            opts = line[1]
            options_list = []

            opts = opts.strip('[]')
            opts = opts.split(', ')

            for o in opts:
                options_list = []
                for i in opts:
                    if i == 'True':
                        options_list.append(True)
                    else:
                        options_list.append(False)

            self.history.append([string, options_list])



class Rules:
    """
    docstring for Rules.

    """

    def __init__(self):
        super(Rules, self).__init__()
        self.I = ['ruleI', 'RuleI', '1']
        self.II = ['ruleII', 'RuleII', '2']
        self.III = ['ruleIII', 'RuleIII', '3']
        self.IV = ['ruleIV', 'RuleIV', '4']

        self.RuleI = "Description"

    # def __repr__:

    def values(self):
        return self.I + self.II + self.III + self.IV

    # def description(self):
    #     return

    def __rpr__(self):
        description = '''
        RuleI:
        RuleII
        RuleIII
        RuleIV
        '''
        return(f'Rules({self.I!r}, {self.II})')

    def __str__(self):
        return 'hi'
