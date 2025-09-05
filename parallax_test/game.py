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

# bg setup
bg_images:list = []
for x in range(1,4):
    bg_image = pygame.image.load(f"{BASE_IMG_PATH}parallax_{x}.png").convert_alpha()
    bg_images.append(bg_image)
bg_width = bg_images[0].get_width()

scroll = 0

while running:

    display.blit(sky_surf, (0, 0))
    scroll += 1

    # Draw bg
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
           
    pygame.display.flip()
    clock.tick(60)