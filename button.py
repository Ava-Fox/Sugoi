import pygame.font

class Button:
    """A class to manage buttons in SUGOI"""
    
    def __init__(self, s_game, text):
        """Initialize"""
        self.screen = s_game.screen
        self.screen_rect = self.screen.get_rect()
        
        #Dimensions
        self.width, self.height = 200, 50
        self.button_color = (159, 226, 191)
        self.text_color = (23, 32, 42 )
        self.font = pygame.font.SysFont(None, 48)
        
        #Rect object
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        
        self._prep_message(text)
        
    def _prep_message(self, text):
        """Turn text into image and center on rect"""
        self.text_image = self.font.render(text, True, self.text_color, self.button_color)
        self.text_image_rect = self.text_image.get_rect()
        self.text_image_rect.center = self.rect.center
        
    def draw_button(self):
        """Draw blank button and draw message"""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.text_image, self.text_image_rect)
        
    def pop(self):
        """Replace button with Sugoi?! image and increase size"""
        # Shrink
        # Turn text image into sugoi logo
        # Increase text size 
        
        