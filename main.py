# Example file showing a basic pygame "game loop"
import pygame
import csv

# pygame setup
pygame.init()
screen_width = 800;
screen_height = 800;
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

world_objects = []

list_of_tiles = []
grass_tile_table = []
def tileset_loader(image_name):
    _ = pygame.image.load('assets/images/' + image_name).convert_alpha()
    for x in range(0,11):
        line = []
        grass_tile_table.append(line)
        for y in range(0,7):
            rect = (x * 16, y * 16, 16, 16)
            line.append(_.subsurface(rect))

def level_loader(level_name):
    with open('levels/' + level_name + '.csv', newline='') as csvfile:
        f = csv.reader(csvfile, delimiter=',')
        for row in f:
            _ = (row[0],row[1])
            world_objects.append(_)

tileset_loader("Grass.png")
level_loader("level_alpha")

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Thanks for playing")

    screen.fill("purple")

    x = 0
    y = 0
    for obj in world_objects:
        screen.blit(grass_tile_table[int(obj[0])][int(obj[1])], (x, y))
        x = x + 16
        if x >= screen_width:
            x = 0
            y += 16

    pygame.draw.rect(screen, "red", [player_pos[0],player_pos[1],10,10])
    # RENDER YOUR GAME HERE
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()