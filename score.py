import pygame
import pygame.freetype
from constants import *

class Score():
    def __init__(self, font):
        self.font = font
        self.points = 0

    def add_point(self):
        self.points += 1

    def draw(self, screen):
        self.font.render_to(screen, (20, 20), f"Score: {self.points}", "white")
