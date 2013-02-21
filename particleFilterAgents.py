# particleFilterAgents.py
# -----------------
# Written for The Agency at Georgia Tech.  The following license is from
# the original project.

# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import Directions
from keyboardAgents import KeyboardAgent
import util

class ParticleFilterAgent(KeyboardAgent):
  """
  An agent controlled by the keyboard.
  """

  def __init__( self, index = 0 ):
    KeyboardAgent.__init__(self, index)
    self.initialized = False;
    
  def getAction( self, state):
    action = KeyboardAgent.getAction(self, state);
    # First time through, initialize the filter
    if self.initialized == False:
        self.initFilter(state)
        self.initialized = True

    # On all movement, step the filter and take an observation
    if action != Directions.STOP:
        print state.getLegalActions(self.index)
        print state.getPacmanPosition()
        self.moveStep()
        self.observeAndResample(state)
        self.computeWeightedMeanPosition()
    return action
        
  def getMove(self, legal):
    return KeyboardAgent.getMove(self, legal);

  def initFilter(self, state):
 
    self.numParticles   = 50;

    # Observation distribution for the smallSearch map
    self.observationDistn = util.Counter()
    self.observationDistn[(1,3)] = 1.0
    self.observationDistn[(4,3)] = 1.0
    self.observationDistn[(7,3)] = 1.0
    self.observationDistn[(10,3)] = 1.0
    self.observationDistn[(13,3)] = 1.0
    self.observationDistn[(16,3)] = 1.0
    self.observationDistn[(18,3)] = 1.0
    self.observationDistn.normalize() 

    # INITIALIZE YOUR PARTICLES AND WEIGHTS HERE
    # self.particles = []
    # self.particleDistn = util.Counter()

  def moveStep(self):
    # MOVE YOUR PARTICLES HERE
    return False
  
  def observeAndResample(self, state):
    legal = state.getLegalActions(self.index)
    if Directions.SOUTH in legal:
      # MAKE AN OBSERVATION, UPDATE THE PARTICLE WEIGHTS, AND RESAMPLE THE
      # PARTICLE POSITIONS
      return False

  def computeWeightedMeanPosition(self):

    x = 0
    y = 0
    # NOTE: Assumes a util.Counter called self.particleDistn that holds the
    # weights indexed by particle location
    for p,d in self.particleDistn.iteritems():
      x += p[0] * d
      y += p[1] * d

    print x, y;
    return (x, y)
