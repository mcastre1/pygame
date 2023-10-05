import pygame

# Class used to create a button in pygame
class Button():
    def __init__(self, text, font_size, text_color, font = None):
        self.text = text
        self.font_size = font_size
        self.text_color = text_color
        self.font = font

        self.button_font = pygame.font.Font(self.font, font_size)
        self.button_text = self.button_font.render(self.text, True, self.text_color)
        self.button_rect = self.button_text.get_rect()

    # Returns the buttons rect, normally used to change the x and y coordinates of such rect.
    def get_button_rect(self):
        return self.button_rect
    
    # Draws 'button' on current pygame screen.
    def blit(self):
        screen = pygame.display.get_surface()
        screen.blit(self.button_text, self.button_rect)