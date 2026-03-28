from rules import Rules
import random

class Simulation(Rules):
    def __init__(self, bet=1):
        super().__init__()
        self.bet = bet
    

    #here user will play
    #have a way to where the user decides when they want to bet (like a buttom or input)
    def simBets(self):
        if random.random() < self.probability:
            self.money += self.bet
        else:
            self.money -= self.bet

    
    def play(self):
        willPlay = input("Would you like to bet y/n?")
        if willPlay == "y":
            self.simBets()
            print("You have $", self.money, "left")
        else:
            print("Ok")

player = Simulation();
player.play();
        


