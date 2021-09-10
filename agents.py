from game import Agent
from game import Directions
from random import randrange
from layout import getLayout

class DumbAgent(Agent):
    "An agent that goes West until it can't."
    def getAction(self, state):
        "The agent always goes West. "
        return Directions.WEST

class RandomAgent(Agent):
    "An agent that takes a random valid action."
    def getAction(self,state):
        "The agent chooses a random direction"
        legalacts = state.getLegalPacmanActions()
        rand = randrange(len(legalacts))
        while legalacts[rand] == Directions.STOP :
            rand = randrange(len(legalacts))
        return legalacts[rand]

class ReflexAgent(Agent):

    def getAction(self, state):

        legalacts = state.getLegalPacmanActions()

        foodcnt = state.getNumFood()

        for a in legalacts :
            succ = state.generatePacmanSuccessor(a)
            if succ.getNumFood() < foodcnt :
                return a

        rand = randrange(len(legalacts))
        while legalacts[rand] == Directions.STOP:
            rand = randrange(len(legalacts))
        return legalacts[rand]