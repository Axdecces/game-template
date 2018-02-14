from Scene import Scene
import pygame

class Scene_Menu(Scene):
    def __init__(self, game):
        Scene.__init__(self, game)

    def init(self):
        pygame.font.init()
        self.font = pygame.font.Font('assets/fonts/Munro.ttf', 30)

    def update(self, delta_time, events):
        pass

    def draw(self, screen):
        pass
