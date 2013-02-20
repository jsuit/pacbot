# particleFilter.py
# -----------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import Agent
from game import Directions
from keyboardAgents import KeyboardAgent
import random

class ParticleFilterAgent(KeyboardAgent):
  """
  An agent controlled by the keyboard.
  """

  def __init__( self, index = 0 ):
    KeyboardAgent.__init__(self, index)
    
  def getAction( self, state):
    return KeyboardAgent.getAction(self, state);

  def getMove(self, legal):
    return KeyboardAgent.getMove(self, legal);
  
