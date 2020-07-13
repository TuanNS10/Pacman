# multiAgents.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """


    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()

        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices) # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)

        #  Lấy trạng thái mới của game sau khi Pacman thực hiện action.
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        #Lấy vị trí của Pacman sau khi Pacman thực hiện action. 
        newPos = successorGameState.getPacmanPosition()
        # Cập nhật phần thức ăn còn lại sau khi Pacman thực hiện action.
        newFood = successorGameState.getFood()
        # Cập nhật trạng thái mới của ma sau khi Pacman thực hiện action.
        newGhostStates = successorGameState.getGhostStates()
        newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

        "*** YOUR CODE HERE ***"
        """tính khoảng cách đến thức ăn xa nhất"""
        newFoodList = newFood.asList()
        min_food_distance = -1
        for food in newFoodList:
            distance = util.manhattanDistance(newPos, food)
            if min_food_distance >= distance or min_food_distance == -1:
                min_food_distance = distance

        """Tính khoảng cách từ pacman đến hồn ma.
         Ngoài ra, kiểm tra sự gần gũi của những con ma (ở khoảng cách 1) xung quanh pacman."""
        distances_to_ghosts = 1
        proximity_to_ghosts = 0
        for ghost_state in successorGameState.getGhostPositions():
            distance = util.manhattanDistance(newPos, ghost_state)
            distances_to_ghosts += distance
            if distance <= 1:
                proximity_to_ghosts += 1

        """Tổng hợp số liệu vừa tìm được sẽ trả về"""
        return successorGameState.getScore() + (1 / float(min_food_distance)) - (1 / float(distances_to_ghosts)) - proximity_to_ghosts
        #return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
        self.index = 0 # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # Đầu tiên, trong thuật toán này, hàm Minimax sẽ có 3 tham số đầu vào 
        #Đó chính là: agent,độ sâu, và trạng thái của game
        def minimax(agent, depth, gameState):
            #Nếu mà trạng thái này thua/thắng hoặc độ sâu của agent bằng độ sau giới hạn trong khung chơi thì
            if gameState.isLose() or gameState.isWin() or depth == self.depth:
                # Trả về giá trị ước lượng của trạng thái mà pacman thực hiện hành động 
                return self.evaluationFunction(gameState)
       # tại đây có 2 trường hợp:
       # 1 là khi agent=0 hoặc trường hợp còn lại
                
            if agent == 0:  # maximize for pacman
                # trả về trạng thái successor của game sau khi agent thực hiện hành động 
                # và trả về các hành động mà agnet có thể thực hiện
                return max(minimax(1, depth, gameState.generateSuccessor(agent, newState)) for newState in gameState.getLegalActions(agent))
            else:  # minize for ghosts
                 # Tính toán các Agent và tăng độ sâu(bước đi của pacman đi)
                nextAgent = agent + 1 
                if gameState.getNumAgents() == nextAgent:
                    nextAgent = 0
                if nextAgent == 0:
                   depth += 1
                   # trả về  chi phi ước lượng ít nhất bằng cách gọi lại hàm
                return min(minimax(nextAgent, depth, gameState.generateSuccessor(agent, newState)) for newState in gameState.getLegalActions(agent))

        """Thực hiện hành động tối đa hoá hành động của pacman"""
        maximum = float("-inf")
        # hướng đi của pacman sẽ là hướng tây
        action = Directions.WEST
        #Trả về các hành động mà agent có thể thực hiện.
        for agentState in gameState.getLegalActions(0):
              # trả về trạng thái successor của game sau khi agent thực hiện hành động
            utility = minimax(1, 0, gameState.generateSuccessor(0, agentState))
            if utility > maximum or maximum == float("-inf"):
                maximum = utility
                action = agentState

        return action

        util.raiseNotDefined()

class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        "*** YOUR CODE HERE ***"
        def maximizer(agent, depth, game_state, a, b):  # maximizer function
            v = float("-inf")
            for newState in game_state.getLegalActions(agent):
                v = max(v, alphabetaprune(1, depth, game_state.generateSuccessor(agent, newState), a, b))
                if v > b:
                    return v
                a = max(a, v)
            return v

        def minimizer(agent, depth, game_state, a, b):  # minimizer function
            v = float("inf")

            next_agent = agent + 1  # Tính toán đại lý tiếp theo và tăng chiều sâu cho phù hợp.
            if game_state.getNumAgents() == next_agent:
                next_agent = 0
            if next_agent == 0:
                depth += 1

            for newState in game_state.getLegalActions(agent):
                v = min(v, alphabetaprune(next_agent, depth, game_state.generateSuccessor(agent, newState), a, b))
                if v < a:
                    return v
                b = min(b, v)
            return v

        def alphabetaprune(agent, depth, game_state, a, b):
            if game_state.isLose() or game_state.isWin() or depth == self.depth:  # Trả lại tiện ích trong trường hợp độ sâu được xác định là đạt hoặc trò chơi được thắng / thua.
                return self.evaluationFunction(game_state)

            if agent == 0:  # Tối đa hóa cho pacman
                return maximizer(agent, depth, game_state, a, b)
            else:  # Giảm thiểu cho ma
                return minimizer(agent, depth, game_state, a, b)

        "" "Thực hiện chức năng công cụ tối đa vào thư mục gốc nút ví dụ: pacman sử dụng tỉa alpha-beta." ""
        utility = float("-inf")
        action = Directions.WEST
        alpha = float("-inf")
        beta = float("inf")
        for agentState in gameState.getLegalActions(0):
            ghostValue = alphabetaprune(1, 0, gameState.generateSuccessor(0, agentState), alpha, beta)
            if ghostValue > utility:
                utility = ghostValue
                action = agentState
            if utility > beta:
                return utility
            alpha = max(alpha, utility)

        return action
        util.raiseNotDefined()

class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        "*** YOUR CODE HERE ***"
        def expectimax(agent, depth, gameState):
            if gameState.isLose() or gameState.isWin() or depth == self.depth:  # Trả lại tiện ích trong trường hợp độ sâu được xác định là đạt hoặc trò chơi được thắng / thua.
                return self.evaluationFunction(gameState)
            if agent == 0:  # Tối đa hóa cho pacman
                return max(expectimax(1, depth, gameState.generateSuccessor(agent, newState)) for newState in gameState.getLegalActions(agent))
            else:  # Thực hiện hành động expectimax cho các nút ma / cơ hội.
                nextAgent = agent + 1  # Tính toán agent tiếp theo và tăng chiều sâu cho phù hợp.
                if gameState.getNumAgents() == nextAgent:
                    nextAgent = 0
                if nextAgent == 0:
                    depth += 1
                return sum(expectimax(nextAgent, depth, gameState.generateSuccessor(agent, newState)) for newState in gameState.getLegalActions(agent)) / float(len(gameState.getLegalActions(agent)))

        "" "Thực hiện nhiệm vụ tối đa hóa cho mục gốc nút ví dụ: pacman" ""
        maximum = float("-inf")
        action = Directions.WEST
        for agentState in gameState.getLegalActions(0):
            utility = expectimax(1, 0, gameState.generateSuccessor(0, agentState))
            if utility > maximum or maximum == float("-inf"):
                maximum = utility
                action = agentState

        return action

        util.raiseNotDefined()

def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction
