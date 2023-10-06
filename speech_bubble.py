import pygame

class Bubble:
    """Class to manage speech bubbles"""
    
    def __init__(self, s_game, image):
        """Initialize attributes"""
        self.image = pygame.image.load('images/bubble.png')
        self.rect = self.image.get_rect()
        self.screen = s_game.screen
        self.screen_rect = self.screen.get_rect()
        self.rect.center = self.screen_rect.center
        
        self._prep_message(image)
        
    def _prep_message(self, image):
        """turn text into image and center on bubble"""
        self.text_image = image
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center
        
    def blitme(self):
        """Blit image to screen"""
        self.screen.blit(self.image, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)