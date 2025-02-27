import pygame
from constants import *
from circleshape import CircleShape


class Asteriod(CircleShape):
    def __init__(self, x, y, radius):


    def draw(self, screen):
        pygame.draw.circle (screen, "white", self.triangle(), 2)