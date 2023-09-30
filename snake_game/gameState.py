from settings import *
from sprites.head import Head
from sprites.apple import Apple
from sprites.body import Body
import random, pygame, sys
from particle import Particle
import json

class GameState():
    def __init__(self, head_group, body_group, pickup_group, screen, apple_bite_sfx, bg_music):
        pygame.mixer.init()
        self.state = "play"
        self.head_group = head_group
        self.body_group = body_group
        self.pickup_group = pickup_group
        self.screen = screen
        self.update_head = pygame.USEREVENT + 1
        self.timer_speed = 200
        self.init = True
        self.head = Head(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
        self.font = pygame.font.Font(None, 20)

        # sounds
        self.apple_bite_sfx = apple_bite_sfx
        self.head_collision = pygame.mixer.Sound('./snake_game/sounds/collision_head.flac')
        self.gameover_music = pygame.mixer.Sound('./snake_game/sounds/gameover.wav')
        self.bg_music = bg_music

        # intro settings
        self.intro_font = pygame.font.Font(None, 100)
        self.snake_text = self.intro_font.render('Snake', True, 'Black')
        self.snake_text_rect = self.snake_text.get_rect()
        self.snake_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/3)

        self.button_font = pygame.font.Font(None, 20)
        self.play_text = self.button_font.render('Play', True, 'Black')
        self.play_text_rect = self.play_text.get_rect()
        self.play_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 100)

        self.highscores_font = pygame.font.Font(None, 30)
        self.highscores_text = self.highscores_font.render('Highscores', True, RED)
        self.highscores_rect = self.highscores_text.get_rect()
        self.highscores_rect.center = (SCREEN_WIDTH/2, (SCREEN_WIDTH/2)+50)

        # pause settings
        self.pause_font = pygame.font.Font(None, 100)
        self.pause_text = self.pause_font.render('PAUSE', True, 'Black')
        self.pause_text_rect = self.pause_text.get_rect()
        self.pause_text_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/3)

        # particles
        self.particles = Particle()

        # saving feature
        self.highscores = {}

        try:
        # Read and load json text file
            with open('./snake_game/highscores.txt', 'r') as highscores_file:
                self.highscores = json.load(highscores_file)
        except:
            print("No file created yet")

    def set_state(self, state):
        self.state = state

    def state_manager(self):
        if self.state == "play":
            if self.init:
                self.play_init()
            self.play()
        elif self.state == 'intro':
            self.intro_state()
        elif self.state == 'pause':
            self.pause_state()
        elif self.state == 'gameover':
            self.gameover_state()
        elif self.state == 'highscores':
            self.highscores_state()

    def play_init(self):
        # Add sprites to groups
        self.head_group.add(self.head)

        # Spawn initial apple
        self.spawnApple()

        pygame.time.set_timer(self.update_head, self.timer_speed)

        self.init = False

    def play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save()
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_p]:
                    print('pause')
                    self.state = 'pause'

            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_DOWN]:
                    self.head.set_direction('Down')
                elif keys[pygame.K_UP]:
                    self.head.set_direction('Up')
                elif keys[pygame.K_LEFT]:
                    self.head.set_direction('Left')
                elif keys[pygame.K_RIGHT]:
                    self.head.set_direction('Right')

            if event.type == self.update_head:
                self.head_group.update()

                if len(self.body_group) > 0:
                    new_body_group = self.body_group.sprites()[:-1]
                    
                    if self.head.direction == 'Right':
                        new_body_group.insert(0, Body(self.head.pos_x-SIZE, self.head.pos_y, self.head.direction))
                    elif self.head.direction == 'Left':
                        new_body_group.insert(0, Body(self.head.pos_x+SIZE, self.head.pos_y, self.head.direction))
                    elif self.head.direction == 'Up':
                        new_body_group.insert(0, Body(self.head.pos_x, self.head.pos_y + SIZE, self.head.direction))
                    elif self.head.direction == 'Down':
                        new_body_group.insert(0,Body(self.head.pos_x, self.head.pos_y - SIZE, self.head.direction))

                    self.body_group = pygame.sprite.Group(new_body_group)

        self.screen.fill(WHITE)
    
        self.pickup_group.draw(self.screen)
        self.head_group.draw(self.screen)
        self.body_group.draw(self.screen)

        self.checkCollision()
        self.particles.emit()
        self.checkOutOfBounds()
        self.updateScore()

    # public method to save current highscores
    def save(self):
        with open('./snake_game/highscores.txt', 'w') as highscores_file:
                json.dump(self.highscores, highscores_file)

    # Check if snake head "touches" the edge of the screen
    # If so, gameover.
    def checkOutOfBounds(self):
        if self.head.direction == 'Right':
            if self.head.rect.right > SCREEN_WIDTH:
                self.state = 'gameover'
        elif self.head.direction == 'Left':
            if self.head.rect.left < 0:
                self.state = 'gameover'
        elif self.head.direction == 'Up':
            if self.head.rect.top < 0:
                self.state = 'gameover'
        elif self.head.direction == 'Down':
            if self.head.rect.bottom > SCREEN_HEIGHT:
                self.state = 'gameover'

        if self.state == 'gameover':
            self.head_collision.play()

    # Update score at top of screen to new score.
    def updateScore(self):
        text = self.font.render(f'Score : {self.head.score}', True, 'Black')
        text_rect = text.get_rect()

        text_rect.center = (SCREEN_WIDTH/2, 20)

        self.screen.blit(text, text_rect)


    # Check whether the snake head has collided with itself or an apple/pickup
    def checkCollision(self):
        # Check collision of head with itself
        # If so, gameover
        for body in self.body_group:
            if body.rect.colliderect(self.head.rect):
                self.head_collision.play()
                self.state = 'gameover'
        
        # Check collision of head with apple/pickup
        # If so, play sound, destroy the pickup, randomly spawn a new pickup on screen,
        # create a new body part for the snake, and add to the current score.
        for pickup in self.pickup_group:
            if self.head.rect.colliderect(pickup.rect):
                self.apple_bite_sfx.play()
                position = pickup.rect.topleft
                self.particles.add_particles(position[0], position[1])
                pickup.kill()
                self.spawnApple()
                
                # Creating a new body part once an apple has been collided against.
                if len(self.body_group) == 0:
                    if self.head.direction == 'Right':
                        self.body_group.add(Body(self.head.pos_x - SIZE, self.head.pos_y, self.head.direction))
                    elif self.head.direction == 'Left':
                        self.body_group.add(Body(self.head.pos_x + SIZE, self.head.pos_y, self.head.direction))
                    elif self.head.direction == 'Up':
                        self.body_group.add(Body(self.head.pos_x, self.head.pos_y + SIZE, self.head.direction))
                    elif self.head.direction == 'Down':
                        self.body_group.add(Body(self.head.pos_x, self.head.pos_y - SIZE, self.head.direction))
                elif len(self.body_group) > 0:
                    tail = self.body_group.sprites()[-1]

                    if tail.direction == 'Right':
                        self.body_group.add(Body(tail.pos_x - SIZE, tail.pos_y, tail.direction))
                    elif tail.direction == 'Left':
                        self.body_group.add(Body(tail.pos_x + SIZE, tail.pos_y, tail.direction))
                    elif tail.direction == 'Up':
                        self.body_group.add(Body(tail.pos_x, tail.pos_y + SIZE, tail.direction))
                    elif tail.direction == 'Down':
                        self.body_group.add(Body(tail.pos_x, tail.pos_y - SIZE, tail.direction))

                self.head.add_score(10)

    def spawnApple(self):
        height_indeces = SCREEN_HEIGHT/SIZE
        width_indeces = SCREEN_WIDTH/SIZE
        # This will ensure apple spawns one index before each of the edges
        apple = Apple(random.randint(1, width_indeces - 1)*SIZE, random.randint(1, height_indeces - 1)*SIZE)

        self.pickup_group.add(apple)
        self.timer_speed -= 1
        pygame.time.set_timer(self.update_head, self.timer_speed)
    
    def pause_state(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save()
                pygame.quit()
                sys.exit()
            
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_p]:
                    self.state = 'play'
        
        
        self.screen.fill(WHITE)

        self.pickup_group.draw(self.screen)
        self.head_group.draw(self.screen)
        self.body_group.draw(self.screen)

        # Surface used to make illusion of grayed out game assets.
        pause_surf = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        pause_surf_rect = pause_surf.get_rect()
        pause_surf.fill(DARK_GRAY)
        # This is how you make the above surface transperent
        pause_surf.set_alpha(128)

        self.screen.blit(pause_surf, pause_surf_rect)

        self.screen.blit(self.pause_text, self.pause_text_rect)

    def intro_state(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save()
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.play_text_rect.collidepoint(pygame.mouse.get_pos()):
                        self.state = 'play'
                    if self.highscores_rect.collidepoint(pygame.mouse.get_pos()):
                        self.state = 'highscores'

            if event.type == pygame.MOUSEMOTION:

                if self.play_text_rect.collidepoint(pygame.mouse.get_pos()):
                    self.play_text = self.button_font.render('Play', True, 'Gray')
                else:
                    self.play_text = self.button_font.render('Play', True, 'Black')
                
                if self.highscores_rect.collidepoint(pygame.mouse.get_pos()):
                    self.highscores_text = self.highscores_font.render('Highscores', True, 'Orange')
                else:
                    self.highscores_text = self.highscores_font.render('Highscores', True, RED)

                

        self.screen.fill(WHITE)
        self.screen.blit(self.highscores_text, self.highscores_rect)

        self.screen.blit(self.snake_text, self.snake_text_rect)
        self.screen.blit(self.play_text, self.play_text_rect)

    def highscores_state(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # highscores
        count = 1

        self.screen.fill(WHITE)

        for key in self.highscores.keys():
            highscore_font = pygame.font.Font(None, 30)
            highscore_text = highscore_font.render(f'{key} ------ {self.highscores[key]}', True, 'black')
            highscore_rect = highscore_text.get_rect()
            highscore_rect.center = (SCREEN_WIDTH/2, (SCREEN_HEIGHT/12) * count)
            count += 1
            self.screen.blit(highscore_text, highscore_rect)
            print(key)

    def gameover_state(self):
        self.bg_music.stop()
        self.gameover_music.play()

        playagain_font = pygame.font.Font(None, 30)
        playagain_text = playagain_font.render('Play again', True, DARK_GRAY)
        playagain_rect = playagain_text.get_rect()
        playagain_rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

        score_font = pygame.font.Font(None, 40)
        score_text = score_font.render(f'Score = {self.head.get_score()}', True, DARK_GRAY)
        score_rect= score_text.get_rect()
        score_rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 - 60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.save()
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if playagain_rect.collidepoint(pygame.mouse.get_pos()):
                        self.gameover_music.stop()
                        self.bg_music.play(-1)
                        self.particles.particles = []
                        self.body_group.empty()
                        self.head_group.empty()
                        self.pickup_group.empty()
                        self.head = Head(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
                        self.init = True
                        self.state = 'play'

        if playagain_rect.collidepoint(pygame.mouse.get_pos()):
            playagain_text = playagain_font.render('Play again', True, 'Gray')
        else:
            playagain_text = playagain_font.render('Play again', True, 'Black')

        playagain_rect = playagain_text.get_rect()
        playagain_rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2)

        # Text surface
        gameover_font = pygame.font.Font(None, 80)
        gameover_text = gameover_font.render('GameOver', True, RED)
        gameover_rect = gameover_text.get_rect()
        gameover_rect.center = (SCREEN_WIDTH/2,SCREEN_HEIGHT/2 - 200)

        self.screen.fill(WHITE)
        self.screen.blit(gameover_text, gameover_rect)
        self.screen.blit(playagain_text, playagain_rect)
        self.screen.blit(score_text, score_rect)


