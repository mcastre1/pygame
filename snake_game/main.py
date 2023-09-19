import pygame, sys
from settings import *
from sprites.head import Head
from sprites.body import Body
from sprites.apple import Apple
import random

pygame.init()
timer_speed = 200
# User event to update head position
update_head = pygame.USEREVENT + 1
pygame.time.set_timer(update_head, timer_speed)

def checkCollision():
    global head_group, body_group, head, tail

    for body in body_group:
        if body.rect.colliderect(head.rect):
            print("Collided")
        
    for pickup in pickup_group:
        if head.rect.colliderect(pickup.rect):
            pickup.kill()
            spawnApple()
            if len(body_group) == 0:
                if head.direction == 'Right':
                    body_group.add(Body(head.pos_x - SIZE, head.pos_y, head.direction))
                elif head.direction == 'Left':
                    body_group.add(Body(head.pos_x + SIZE, head.pos_y, head.direction))
                elif head.direction == 'Up':
                    body_group.add(Body(head.pos_x, head.pos_y + SIZE, head.direction))
                elif head.direction == 'Down':
                    body_group.add(Body(head.pos_x, head.pos_y - SIZE, head.direction))
            else:
                tail = body_group.sprites()[-1]

                if head.direction == 'Right':
                    body_group.add(Body(tail.pos_x - SIZE, tail.pos_y, tail.direction))
                elif head.direction == 'Left':
                    body_group.add(Body(tail.pos_x + SIZE, tail.pos_y, tail.direction))
                elif head.direction == 'Up':
                    body_group.add(Body(tail.pos_x, tail.pos_y + SIZE, tail.direction))
                elif head.direction == 'Down':
                    body_group.add(Body(tail.pos_x, tail.pos_y - SIZE, tail.direction))

def spawnApple():
    global pickup_group, timer_speed
    height_indeces = SCREEN_HEIGHT/SIZE
    width_indeces = SCREEN_WIDTH/SIZE

    pickup_group.add(Apple(random.randint(0, width_indeces)*SIZE, random.randint(0, height_indeces)*SIZE))
    timer_speed -= 1
    pygame.time.set_timer(update_head, timer_speed)


clock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Sprites
head = Head(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

# Sprite groups
head_group = pygame.sprite.Group()
body_group = pygame.sprite.Group()
pickup_group = pygame.sprite.Group()

# Add sprites to groups
head_group.add(head)

# Spawn initial apple
spawnApple()
#pickup_group.add(Apple(random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT)))




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                head.set_direction('Down')
            elif keys[pygame.K_UP]:
                head.set_direction('Up')
            elif keys[pygame.K_LEFT]:
                head.set_direction('Left')
            elif keys[pygame.K_RIGHT]:
                head.set_direction('Right')
        if event.type == update_head:
            head_group.update()
            new_body_group = body_group.sprites()[:-1]
            
            if head.direction == 'Right':
                new_body_group.insert(0, Body(head.pos_x-SIZE, head.pos_y, head.direction))
            elif head.direction == 'Left':
                new_body_group.insert(0, Body(head.pos_x+SIZE, head.pos_y, head.direction))
            elif head.direction == 'Up':
                new_body_group.insert(0, Body(head.pos_x, head.pos_y + SIZE, head.direction))
            elif head.direction == 'Down':
                new_body_group.insert(0,Body(head.pos_x, head.pos_y - SIZE, head.direction))
            body_group = pygame.sprite.Group(new_body_group)

    screen.fill(WHITE)
    
    

    pickup_group.draw(screen)
    head_group.draw(screen)
    body_group.draw(screen)
    

    
    checkCollision()

    pygame.display.update()

    clock.tick(30)