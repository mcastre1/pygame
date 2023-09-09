import pygame
import sys

class GameState():
    def __init__(self, crosshair, screen, target_group, crosshair_group, screen_width, screen_height):
        self.state = 'intro'
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.crosshair = crosshair
        self.screen = screen
        self.target_group = target_group
        self.crosshair_group = crosshair_group
        # Font 
        self.font = pygame.font.SysFont("arial", 20)

    def state_manager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'main_game':
            self.main_game()


    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'


        pygame.display.flip()
        #screen.blit(background,(0,0))
        self.screen.fill((255,255,255))
        ready_text = self.font.render('Ready?', True, (0,0,0))
        text_rect = ready_text.get_rect()

        text_rect.center = (self.screen_width/2, self.screen_height/2)

        self.screen.blit(ready_text, text_rect)

        self.crosshair_group.draw(self.screen)
        self.crosshair_group.update()


    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.crosshair.shoot(self.crosshair, self.target_group)


        pygame.display.flip()
        #screen.blit(background,(0,0))
        self.screen.fill((255,255,255))
        self.target_group.draw(self.screen)

        self.crosshair_group.draw(self.screen)
        self.crosshair_group.update()
        