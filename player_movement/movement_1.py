import pygame, sys
pygame.init()

SCREEN_SIZE:tuple = (600, 600)

screen = pygame.display.set_mode(SCREEN_SIZE)
clock = pygame.time.Clock()
running = True
movement = [False, False, False, False]
pos = [SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2]

player_surf = pygame.Surface((50, 50))
player_rect = player_surf.get_frect(topleft=pos)

while running:

    frame_movement = (movement[1] - movement[0], movement[3] - movement[2])
    frame_movement = pygame.math.Vector2(frame_movement)
    if frame_movement.magnitude() != 0:
        frame_movement = frame_movement.normalize()

    player_rect.x += frame_movement[0]
    player_rect.y += frame_movement[1]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement[0] = True
            if event.key == pygame.K_RIGHT:
                movement[1] = True
            if event.key == pygame.K_UP:
                movement[2] = True
            if event.key == pygame.K_DOWN:
                movement[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movement[0] = False
            if event.key == pygame.K_RIGHT:
                movement[1] = False
            if event.key == pygame.K_UP:
                movement[2] = False
            if event.key == pygame.K_DOWN:
                movement[3] = False

    print(player_rect.center)

    player_surf.fill('white')
    screen.blit(player_surf, player_rect)
    pygame.display.flip()
    clock.tick(60)

def player_movement(movement=(0,0)):
    frame_movement = movement
    frame_movement = pygame.math.Vector2(movement)
    if frame_movement.magnitude() != 0:
        frame_movement = frame_movement.normalize()

