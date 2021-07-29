# Importing extensions - ep 1, ep 6
# ep 1
import pygame
# ep 6
import random
# ep 12
import math
# ep 15
from pygame import mixer

# Initialize pygame - ep 1
pygame.init()

# Enemy - ep 7
enemyImg = list()
enemyX = list()
enemyY = list()
enemyX_change = list()
enemyY_change = list()
num_of_enemies = 15

# Enemy spawn - ep 13
for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(50 * ((i - 1) % 15) + 18)
    enemyY.append(50 * math.floor(i / 15) + 50)
    enemyX_change.append(3)
    enemyY_change.append(40)

# Create the screen - ep 1
screen = pygame.display.set_mode((800, 600))

# Title and Icon - ep 2
pygame.display.set_caption('Space Invaders')
icon = pygame.image.load('ufo (4).png')
pygame.display.set_icon(icon)

# Score - ep 14
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game Over
game_over = False


def score_text(x, y):
    score = font.render('Score: ' + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Score - the finale ep
gg_font = pygame.font.Font('freesansbold.ttf', 64)


def game_over_text():
    gg = font.render('Game Over', True, (255, 255, 255))
    screen.blit(gg, (200, 250))


# Player - ep 3
playerImg = pygame.image.load('space-invaders (2).png')
playerX = 370
playerY = 480
playerX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y, z):
    screen.blit(enemyImg[z], (x, y))


# Background - ep 9
background = pygame.image.load('background1 (1).png')

# Background music - ep 15
mixer.music.load('background.wav')
mixer.music.play(-1)

# Bullet - ep 10
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 490
bulletY_change = 10
bullet_is_fired = False


def fire_bullet(x, y):
    global bullet_is_fired
    bullet_is_fired = True
    screen.blit(bulletImg, (x + 16, y))


# Collision - ep 12
def is_collision(x1, y1, x2, y2):
    distance = math.sqrt(math.pow(x1 - x2, 2) + math.pow(y1 - y2, 2))
    if distance < 27:
        return True


# Game Loop - ep 1
running = True
while running:

    # RGB - ep 2
    screen.fill((26, 26, 26))

    # Draw background - ep 9
    screen.blit(background, (0, 0))

    # Events - ep 1
    for event in pygame.event.get():

        # Quit game - ep 1
        if event.type == pygame.QUIT:
            running = False

        # Controls - ep 5, 10
        if event.type == pygame.KEYDOWN:
            # ep 5
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                playerX_change = -5
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                playerX_change = 5

            # ep 10
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                # ep 11
                if not bullet_is_fired:
                    bullet_sound = mixer.Sound('laser.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, playerY)
        if event.type == pygame.KEYUP:
            # ep 5
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change

    # Boundaries - ep 6
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    # Bullet movement - ep 10
    if bullet_is_fired:
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

        # Bullet reset - ep 11
        if bulletY <= 0:
            bulletY = 480
            bullet_is_fired = False

    # Draw player - ep 3
    player(playerX, playerY)

    # Enemy movement - ep 8
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        # Collision - ep 12
        collision = is_collision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_is_fired = False
            score_value += 100
            enemyX[i] = 50 * random.randint(0, 14) + 18
            enemyY[i] = 50 * random.randint(0, 2) + 18
        if enemyY[i] > 430:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over = True
        # Enemy
        enemy(enemyX[i], enemyY[i], i)

    # Draw score - ep 14
    score_text(textX, textY)

    # Updating - ep 2
    pygame.display.update()
    if game_over:
        break

running2 = True
if game_over:
    while running2:
        game_over_text()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running2 = False
