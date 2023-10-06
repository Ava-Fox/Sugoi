import pygame
from pygame.sprite import Sprite

class Heart(Sprite):
    """A class to manage the throbbing heart rain in beginning of Sugoi?!"""
    
    def __init__(self, s_game):
        """Initialize individual heart's attributions"""
        super().__init__()
        self.screen = s_game.screen
        self.settings = s_game.settings
        
        self.image = pygame.image.load('images/heart.png')
        self.rect = self.image.get_rect()
        
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        
        # Store exact positions
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        
    def check_edges(self):
        """Return True if heart at edge of screen"""
        screen_rect = self.screen.get_rect()
        return (self.rect.top >= screen_rect.bottom)
    
    def update(self):
        """Move heart-drop down"""
        self.rect.y += self.settings.raindrop_speed
        
        