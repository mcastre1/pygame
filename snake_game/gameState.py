from settings import *
from sprites.head import Head
from sprites.apple import Apple
from sprites.body import Body
import random, pygame, sys

class GameState():
    def __init__(self, head_group, body_group, pickup_group, screen):
        self.state = "play"
        self.head_group = head_group
        self.body_group = body_group
        self.pickup_group = pickup_group
        self.screen = screen
        self.update_head = pygame.USEREVENT + 1
        self.timer_speed = 200
        self.init = True

    def state_manager(self):
        if self.state == "play":
            if self.init:
                self.play_init()
            self.play()

    def play_init(self):
        # Sprites
        self.head = Head(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        # Add sprites to groups
        self.head_group.add(self.head)

        # Spawn initial apple
        self.spawnApple()

        pygame.time.set_timer(self.update_head, self.timer_speed)

        self.init = False

    def play(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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

        pygame.display.update()

    def checkCollision(self):
        for body in self.body_group:
            if body.rect.colliderect(self.head.rect):
                print("Collided")
            
        for pickup in self.pickup_group:
            if self.head.rect.colliderect(pickup.rect):
                pickup.kill()
                self.spawnApple()
                if len(self.body_group) == 0:
                    if self.head.direction == 'Right':
                        self.body_group.add(Body(self.head.pos_x - SIZE, self.head.pos_y, self.head.direction))
                    elif self.head.direction == 'Left':
                        self.body_group.add(Body(self.head.pos_x + SIZE, self.head.pos_y, self.head.direction))
                    elif self.head.direction == 'Up':
                        self.body_group.add(Body(self.head.pos_x, self.head.pos_y + SIZE, self.head.direction))
                    elif self.head.direction == 'Down':
                        self.body_group.add(Body(self.head.pos_x, self.head.pos_y - SIZE, self.head.direction))
                else:
                    tail = self.body_group.sprites()[-1]

                    if self.head.direction == 'Right':
                        self.body_group.add(Body(tail.pos_x - SIZE, tail.pos_y, tail.direction))
                    elif self.head.direction == 'Left':
                        self.body_group.add(Body(tail.pos_x + SIZE, tail.pos_y, tail.direction))
                    elif self.head.direction == 'Up':
                        self.body_group.add(Body(tail.pos_x, tail.pos_y + SIZE, tail.direction))
                    elif self.head.direction == 'Down':
                        self.body_group.add(Body(tail.pos_x, tail.pos_y - SIZE, tail.direction))

            

    def spawnApple(self):
        height_indeces = SCREEN_HEIGHT/SIZE
        width_indeces = SCREEN_WIDTH/SIZE
        # This will ensure apple spawns one index before each of the edges
        apple = Apple(random.randint(1, width_indeces - 1)*SIZE, random.randint(1, height_indeces - 1)*SIZE)

        self.pickup_group.add(apple)
        self.timer_speed -= 1
        print(f" New timer speed : {self.timer_speed}")
        pygame.time.set_timer(self.update_head, self.timer_speed)