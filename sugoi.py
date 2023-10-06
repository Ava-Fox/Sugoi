import sys
from time import sleep

import pygame
from pygame.sprite import Sprite

from settings import Settings
from characters import Andy
from heart import Heart
from speech_bubble import Bubble
from button import Button

class Sugoi:
    """Overall class to manage game behavior"""
  
    def __init__(self):
        """Initialize and create game resources"""
    
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
            self.settings.screen_height))
        self.screen_rect = self.screen.get_rect()
        pygame.display.set_caption("Sugoi?!")
        self.bg_color = self.settings.background_color
        
        self.andy = Andy(self)
        
        self._prep_speech_bubble()
        
        self.droplets = pygame.sprite.Group()
        self._create_rain()
        
        self._initialize_play_button()
        
        self.opening_scene = True
        self.game_running = False
        
    
    def run_game(self):
        """Start w/ main loop for game"""
        while True:
            self._check_events()
            self._run_opening_scene()
            
            if self.game_running: 
                self.opening_scene = False
                pass
                
            self._update_screen()
            self.clock.tick(60)
            
    def _prep_speech_bubble(self):
        """Prep initial opening sequence speech bubble"""
        adventure = pygame.image.load('images/adv_txt.png')
        self.bubble = Bubble(self, adventure)
        self.bubble.rect.x = self.screen_rect.left + 50
        self.bubble.rect.y = 50
        self.bubble.text_image_rect.center = self.bubble.rect.center 
        self.bubble.text_image_rect.y -= 25
        
    def _initialize_play_button(self):
        """Set up play button"""
        self.play_button = Button(self, '"Yes!"')
        self.play_button.rect.y = self.settings.screen_height - 2 * self.play_button.rect.height
        self.play_button.text_image_rect.center = self.play_button.rect.center
      
    def _check_events(self):
        """Watch for keyboard/mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_button(mouse_pos)
                
    def _check_button(self, mouse_pos):
        """Start new game when player clicks 'yes'"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        
        if button_clicked and not self.game_running:
            # Somehow add a 'depressed' button image when mousebutton clicked
            self._start_game()
            
                
    def _check_keydown_events(self, event):
        """Watch for keypresses"""
        if event.key == pygame.K_q:
            sys.exit()
    
    def _start_game(self):
        """Start new game"""
        # Eventually, Sugoi logo pop-up 
        self.opening_scene = False
        self.game_running = True
                
    def _create_rain(self):
        """
        Make droplet and keeping until no more room
        Space between droplets is one droplet width
        """
        droplet = Heart(self)
        droplet_width, droplet_height = droplet.rect.size
        
        current_x, current_y = droplet_width, droplet_height
        while current_y < self.settings.screen_height:
            while current_x < (self.settings.screen_width - droplet_width):
                self._create_droplet(current_x, current_y)
                current_x += 2 * droplet_width
                
            # Finished row, reset x_value and increment y value
            current_x = droplet_width
            current_y += 2 * droplet_height
        
    def _run_opening_scene(self):
        """Run title sequence before player clicks play"""
        if not self.andy.in_position():
            self.andy.move_left()
        self._update_rain()
        
    def _update_rain(self):
        """Update positions of all droplets in heart-rain"""
        self._check_rain_edges()
        self.droplets.update()
        
    def _check_rain_edges(self):
        """
        Check to see if droplet has reached edge of screen
        Create new row of droplets at top of screen
        Delete disappeared droplets
        """
        for droplet in self.droplets.sprites():
            if droplet.check_edges():
                self._create_droplet(droplet.rect.x, 0)
                self.droplets.remove(droplet)
                
    def _create_droplet(self, x_position, y_position):
        """Create droplet and place in row"""
        new_droplet = Heart(self)
        new_droplet.x = x_position
        new_droplet.rect.x = x_position
        new_droplet.rect.y = y_position
        self.droplets.add(new_droplet)
        
    def _update_screen(self):
        """Keep screen up to date"""
        self.screen.fill(self.bg_color)
        if self.opening_scene:
            self._update_opening_scene()
        
        pygame.display.flip()
        
    def _update_opening_scene(self):
        """Update screen for opening scene sequence"""
        if self.andy.in_position():
            self.droplets.draw(self.screen)
        self.andy.blitme()
        if self.andy.in_position():
            self.bubble.blitme()
            self.play_button.draw_button()              
                
if __name__ == '__main__':
    s = Sugoi()
    s.run_game()
      