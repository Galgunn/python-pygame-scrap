import pygame, sys

pygame.init()

SCREEN_SIZE:tuple = (500, 500)
ASSET_BCKGRND_SIZE:tuple = (128, 160)
BASE_IMG_PATH:str = 'parallax_test/assets/'

screen:pygame.Surface = pygame.display.set_mode(SCREEN_SIZE)
display:pygame.Surface = pygame.Surface(ASSET_BCKGRND_SIZE)
clock = pygame.time.Clock()
running: bool = True

sky_surf:pygame.Surface = pygame.image.load(BASE_IMG_PATH + 'sky.png').convert_alpha()

# Player movement
player_surf = pygame.Surface((50, 50))
player_rect = player_surf.get_frect(topleft=(SCREEN_SIZE[0] / 2, SCREEN_SIZE[1] / 2))
movement = [False, False]

# bg setup
bg_images:list = []
for x in range(1,4):
    bg_image = pygame.image.load(f"{BASE_IMG_PATH}parallax_{x}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

scroll = 0

while running:

    # Movement
    frame_movement = (movement[1] - movement[0])
    frame_movement = pygame.math.Vector2(frame_movement)
    if frame_movement.magnitude() != 0:
        frame_movement = frame_movement.normalize()

    # Camera movement
    scroll += frame_movement[0]

    # Draw bg
    display.blit(sky_surf, (0, 0))
    for x in range(5): # in charge of blitting the bg image 5 times
        speed = 1
        for img in bg_images:
            display.blit(img, ((x * bg_width) - scroll * speed, 0))
            speed += 0.4
    pygame.transform.scale(display, SCREEN_SIZE, screen)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Movement event handler
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement[0] = True
            if event.key == pygame.K_RIGHT:
                movement[1] = True
            # if event.key == pygame.K_UP:
            #     movement[2] = True
            # if event.key == pygame.K_DOWN:
            #     movement[3] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                movement[0] = False
            if event.key == pygame.K_RIGHT:
                movement[1] = False
            # if event.key == pygame.K_UP:
            #     movement[2] = False
            # if event.key == pygame.K_DOWN:
            #     movement[3] = False

   
    player_surf.fill('white')
    screen.blit(player_surf, player_rect)           
    pygame.display.flip()
    clock.tick(60)