import pygame.font

class Button:

    def __init__(self, ai_game, msg):
        """Initialize the button attributes"""

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        #Set button dimensions and properties of the button
        self.width, self.height = 200, 50
        self.button_color = (224, 63, 52)
        self.text_color = (0,0,0)
        self.font = pygame.font.SysFont(None, 48)

        #Build the button's rect and center it
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        #Button message needs to be prepped only once
        self._prep_msg(msg)


    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on button"""

        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    
    def draw_button(self):
        #Draw a blank button and then draw the message

        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)