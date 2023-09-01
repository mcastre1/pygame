import pygame, sys
import random

def ball_animation():
    global ball_speed_x
    global ball_speed_y
    global opponent_score, player_score
    global ball_speed

    ball.x += ball_speed_x
    ball.y += ball_speed_y

    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Re center / Re spawn ball
    if ball.left <= 0 or ball.right >= screen_width:
        ball_speed_x = ball_speed * random.choice((1,-1))
        ball_speed_y = ball_speed * random.choice((1,-1))

        if ball.left <= 0:
            player_score += 1
        if ball.right >= screen_width:
            opponent_score += 1

        ball.x = screen_width / 2 - 15
        ball.y = screen_height / 2 - 15

    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x *= -1

def opponent_animation():
    global opponent_speed
    if ball.top < opponent.top:
        opponent.y -= opponent_speed
    if ball.bottom > opponent.bottom:
        opponent.y += opponent_speed

def player_animation():
    if player.top <= 0:
        player.top = 0
    if player.bottom >= screen_height:
        player.bottom = screen_height

def update_score():
    global opponent_score, player_score, font, screen

    text = font.render(f'{opponent_score} | {player_score}', True, light_grey)

    textRect = text.get_rect()

    textRect.center = (screen_width/2, textRect.height/2)

    screen.blit(text, textRect)

# General setup
pygame.init()
clock = pygame.time.Clock()

# setting up the main window
screen_width = 1280
screen_height = 960
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Pong')

# Game rectangles
ball = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height/2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200,200,200)

ball_speed = 3

ball_speed_x = ball_speed * random.choice((1,-1))
ball_speed_y = ball_speed * random.choice((1,-1))

player_speed = 0
player_score = 0

opponent_score = 0
opponent_speed = 4

# Font 
font = pygame.font.SysFont("arial", 20)

game_over = False


# loop
while True:
    # handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit() 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7
        if event.type == 771: # key for y
            if game_over:
                ball_speed_x = 7
                ball_speed_y = 7
                opponent_speed = 7
                opponent_score = 0
                player_score = 0



    # Ball collision and movement
    ball_animation()

    # player movement and out of screen collision
    player.y += player_speed
    player_animation()

    opponent_animation()

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width/2,0), (screen_width/2, screen_height))

    
    update_score()

    if opponent_score == 3 or player_score == 3:
        game_over = True
        winningtext = font.render('Game over! Play again? (y/n)', True, light_grey)
        winningtextRect = winningtext.get_rect()

        winningtextRect.center = (screen_width/2, screen_height/2-50)

        screen.blit(winningtext, winningtextRect)

        ball_speed_x = 0
        ball_speed_y = 0
        opponent_speed = 0

# updating the window
    pygame.display.flip()
    clock.tick(60)