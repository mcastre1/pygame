import pygame, sys, json

screen_width = 600
screen_height = 400

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))

clock = pygame.time.Clock()
game_font = pygame.font.Font(None, 32)

# Rectangles
red_surface = pygame.Surface([200, 200])
red_surface.fill((240, 80, 54))
red_rect = red_surface.get_rect(center = (150,180))

blue_surface = pygame.Surface([200,200])
blue_surface.fill((0, 123, 194))
blue_rect = blue_surface.get_rect(center = (450, 180))

# Data
data = {
    'red' : 0,
    'blue' : 0
}

# Read and load json text file
with open('./saving_feature/clicker_score.txt', 'r') as score_file:
    data = json.load(score_file)

# Text
red_score_surface = game_font.render(f'Clicks: {data["red"]}', True, 'Black')
red_score_rect = red_score_surface.get_rect(center = (150,320))

blue_score_surface = game_font.render(f'Clicks: {data["blue"]}', True, 'Black')
blue_score_rect = blue_score_surface.get_rect(center=(450,320))

while True:
    for event in pygame.event.get():
        # When exiting game, save the data scores into a json text file
        if event.type == pygame.QUIT:
            with open('./saving_feature/clicker_score.txt', 'w') as score_file:
                json.dump(data, score_file)
            
            pygame.quit()
            sys.exit()

        # Update data entries with a plus one on event position
        if event.type == pygame.MOUSEBUTTONDOWN:
            if red_rect.collidepoint(event.pos):
                data['red'] += 1
                red_score_surface = game_font.render(f'Clicks: {data["red"]}', True, 'Black')
                red_score_rect = red_score_surface.get_rect(center = (150,320))                

            elif blue_rect.collidepoint(event.pos):
                data['blue'] += 1
                blue_score_surface = game_font.render(f'Clicks: {data["blue"]}', True, 'Black')
                blue_score_rect = blue_score_surface.get_rect(center=(450,320))

    screen.fill((245,255,252))

    screen.blit(red_surface, red_rect)
    screen.blit(blue_surface, blue_rect)

    screen.blit(red_score_surface, red_score_rect)
    screen.blit(blue_score_surface, blue_score_rect)

    pygame.display.update()
    clock.tick(60)