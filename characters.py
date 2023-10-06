"""Manage characters for sugoi"""

import pygame 

class Andy:
    """A class to manage character Andy in Sugoi"""
    
    def __init__(self, s_game):
        """Initialize Andy's characteristics"""
        self.screen = s_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = s_game.settings
        
        self.image = pygame.image.load('images/aa_MED.png') 
        self.rect = self.image.get_rect()
        self.rect.bottomright == self.rect.width
        self.rect.bottomleft = self.screen_rect.bottomright
    
    def blitme(self):
        """Blit image to screen"""
        self.screen.blit(self.image, self.rect)
        
    def move_left(self):
        """
        Move characters from offscreen slowly to left until 
        rightmost side reaches edge of screen
        """
        self.rect.x -= 2
        
    def in_position(self):
        """Return true if pic is in correct position"""
        return (self.rect.bottomright == self.screen_rect.bottomright)
        