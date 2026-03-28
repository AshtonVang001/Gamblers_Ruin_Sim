from rules import Rules
import random

class Simulation(Rules):
    def __init__(self, bet=1, rounds=0):
        super().__init__()
        self.bet = bet
        self.rounds = rounds
    

    def simBets(self):
        if random.random() < self.probability:
            self.money += self.bet
        else:
            self.money -= self.bet

    def play(self):
        willPlay = input("Would you like to play y/n?")
        if(willPlay == "y"):
            while(self.money != self.goal and self.money != self.lose_condition): 
                willBet = input("Would you like to bet y/n?")
                if willBet == "y":
                    self.rounds += 1
                    self.simBets()
                    print("You have $", self.money, "left")
                else:
                    print("Ok")
                    break;
        print("Money left: ", self.money)
        print("Rounds played: ", self.rounds)

player = Simulation();
player.play();
        


