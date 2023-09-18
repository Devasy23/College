class NonTerminal:
    def __init__(self, name):
        self.name = name
        self.rules = []

    def add_rule(self, rule):
            """
            Adds a rule to the list of rules.

            Args:
                rule: A string representing the rule to be added.

            Returns:
                None
            """
            self.rules.append(rule)

    def set_rules(self, rules):
        self.rules = rules

    def get_name(self):
        return self.name

    def get_rules(self):
        return self.rules

    def print_rule(self):
        print(f"{self.name} -> {' | '.join(self.rules)}")


class Grammar:
    def __init__(self):
        self.non_terminals = []

    def add_rule(self, rule):
        nt = False
        parse = ""

        for i in range(len(rule)):
            c = rule[i]
            if c == " ":
                if not nt:
                    new_non_terminal = NonTerminal(parse)
                    self.non_terminals.append(new_non_terminal)
                    nt = True
                    parse = ""
                elif parse != "":
                    self.non_terminals[-1].add_rule(parse)
                    parse = ""
            elif c not in ["|", "-", ">"]:
                parse += c
        if parse != "":
            self.non_terminals[-1].add_rule(parse)

    def input_data(self):
        self.add_rule("A -> BC | a")
        self.add_rule("B -> CA | Ab")
        self.add_rule("C -> AB | CC | a")
    
    def input_data_from_file(self, filepath):
        with open(filepath, 'r') as f:
            for line in f:
                self.add_rule(line.strip())
 

    def solve_non_immediate_lr(self, a, b):
        name_a = a.get_name()
        name_b = b.get_name()

        new_rules_a = []
        rules_a = a.get_rules()
        rules_b = b.get_rules()

        for rule in rules_a:
            if rule.startswith(name_b):
                for rule1 in rules_b:
                    new_rules_a.append(rule1 + rule[len(name_b) :])
            else:
                new_rules_a.append(rule)
        a.set_rules(new_rules_a)

    def solve_immediate_lr(self, a):
        name = a.get_name()
        new_name = name + "'"

        alphas = []
        betas = []
        rules = a.get_rules()
        new_rules_a = []
        new_rules_a1 = []

        for rule in rules:
            if rule.startswith(name):
                alphas.append(rule[len(name) :])
            else:
                betas.append(rule)

        if not alphas:
            return

        if not betas:
            new_rules_a.append(new_name)

        for beta in betas:
            new_rules_a.append(beta + new_name)

        for alpha in alphas:
            new_rules_a1.append(alpha + new_name)

        a.set_rules(new_rules_a)
        new_rules_a1.append("\u03B5")

        new_non_terminal = NonTerminal(new_name)
        new_non_terminal.set_rules(new_rules_a1)
        self.non_terminals.append(new_non_terminal)

    def apply_algorithm(self):
        size = len(self.non_terminals)
        for i in range(size):
            for j in range(i):
                self.solve_non_immediate_lr(self.non_terminals[i], self.non_terminals[j])
            self.solve_immediate_lr(self.non_terminals[i])

    def print_rules(self, filepath):
        with open(filepath, 'w', encoding='utf-8') as f:
            for non_terminal in self.non_terminals:
                f.write(non_terminal.get_name() + " -> " + " | ".join(non_terminal.get_rules()) + "\n")


grammar = Grammar()
grammar.input_data_from_file("p4_input.txt")
grammar.apply_algorithm()
grammar.print_rules("p4_output.txt")