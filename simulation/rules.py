#rules class
class Rules:
    def __init__(self, money=10, goal=20, lose_condition=0, probability=0.5):
        self.money = money
        self.goal = goal
        self.lose_condition = lose_condition
        self.probability = probability

    def printRules(self):
        print(self.money, self.goal, self.lose_condition, self.probability)



me = Rules()
me.printRules()
