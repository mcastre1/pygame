import pygame, sys
from settings import *
from sprites.head import Head
from sprites.body import Body

def checkCollision():
    global head_group, body_group, head

    for body in body_group:
        if body.rect.colliderect(head.rect):
            print("Collided")
        

pygame.init()
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

            if keys[pygame.K_SPACE]:
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
                    direction = tail.direction

                    if head.direction == 'Right':
                        body_group.add(Body(tail.pos_x - SIZE, tail.pos_y, tail.direction))
                    elif head.direction == 'Left':
                        body_group.add(Body(tail.pos_x + SIZE, tail.pos_y, tail.direction))
                    elif head.direction == 'Up':
                        body_group.add(Body(tail.pos_x, tail.pos_y + SIZE, tail.direction))
                    elif head.direction == 'Down':
                        body_group.add(Body(tail.pos_x, tail.pos_y - SIZE, tail.direction))


    screen.fill(WHITE)
    last_pos_x = head.pos_x
    last_pos_y = head.pos_y
    last_direction = head.direction

    head_group.update()

    head_group.draw(screen)
    body_group.draw(screen)

    new_body_group = body_group.sprites()[:-1]

    if head.direction == 'Right':
        new_body_group.insert(0, Body(last_pos_x, last_pos_y, last_direction))
    elif head.direction == 'Left':
        new_body_group.insert(0, Body(last_pos_x, last_pos_y, last_direction))
    elif head.direction == 'Up':
        new_body_group.insert(0, Body(last_pos_x, last_pos_y, last_direction))
    elif head.direction == 'Down':
        new_body_group.insert(0,Body(last_pos_x, last_pos_y, last_direction))

    body_group = pygame.sprite.Group(new_body_group)

    checkCollision()

    pygame.display.update()

    clock.tick()