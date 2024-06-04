# Example file showing a basic pygame "game loop"
import pygame
import csv

# pygame setup
pygame.init()
screen_width = 900;
screen_height = 720;
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

world_objects = []

with open('levels/level_001.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    for row in spamreader:
        world_objects.append(row)
        print(row)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            print("Thanks for playing")

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    for obj in world_objects:
        pygame.draw.rect(screen,"blue", [int(obj[0]),int(obj[1]),int(obj[2]),int(obj[3])])


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