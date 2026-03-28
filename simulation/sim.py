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

    #right now player money is not saving
    #need state for the money
    #also right now game is stopping after each bet - which should not happen
    #game should only stop when player wants it to, they run out of money, or they reach the goal
    def play(self):
        willPlay = input("Would you like to play y/n?")
        if(willPlay == "y"):
            while(self.money != self.goal and self.money != self.lose_condition): #this is the wrong loop
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
        


