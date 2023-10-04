import pygame

class Button():
    def __init__(self, text, font_size, text_color, font = None):
        self.text = text
        self.font_size = font_size
        self.text_color = text_color
        self.font = font

        self.button_font = pygame.font.Font(self.font, font_size)
        self.button_text = self.button_font.render(self.text, True, self.text_color)
        self.button_rect = self.button_text.get_rect()

    def get_button_rect(self):
        return self.button_rect
    
    def blit_button(self):
        screen = pygame.display.get_surface()
        screen.blit(self.button_text, self.button_rect)