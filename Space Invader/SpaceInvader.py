import pygame, random, math
from pygame import mixer

pygame.init()

# screen
screen_width = 900
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
pygame.display.set_caption('Space Invader')

# Set icon
icon = pygame.image.load('Logo.png')
pygame.display.set_icon(icon)

# Background Image and Music
backgroundImg = pygame.image.load('Space.gif')
backgroundImg = pygame.transform.scale(backgroundImg,[screen_width,screen_height])
mixer.music.load('backgroundMusic.wav')
mixer.music.play(-1)

#Player Position
player = pygame.image.load('Player.png')
playerX = 430
playerY = 480
playerX_change = 0

#Bullets Positions
bullet = pygame.image.load('Bullet.png')
bulletX = 0
bulletY = 480
bulletY_change = 10
bullet_state = 'ready'

#Aliens Position
total_aliens = 10
alien, alienX, alienY, alienX_change = [], [], [], []
for i in range(total_aliens):
    alien.append(pygame.image.load('Alien.png'))
    alienX.append(random.randint(0, 836))
    alienY.append(random.randint(0, 150))
    alienX_change.append(random.choice([-1.5, 1.6, 1.7, -1.8]))
alienY_change = 40


def playerShip(player_x, player_y):
    screen.blit(player, [player_x, player_y])

def bulletFire(bullet_x, bullet_y):
    global bullet_state
    bullet_state = 'fired'
    screen.blit(bullet, [bullet_x + 16, bullet_y])

def alienShip(alien_x, alien_y, i):
    screen.blit(alien[i], [alien_x, alien_y])

def isCollision(bullet_x, bullet_y, alien_x, alien_y):
    distance = math.sqrt(math.pow(alien_x - bullet_x, 2) + math.pow(alien_y - bullet_y, 2))
    if distance <= 27:
        return True

scoreValue = 0
font = pygame.font.Font('freesansbold.ttf', 25)
scoreX = 10
scoreY = 10

def show_score(score_x, score_y):
    score = font.render('Score: ' + str(scoreValue), True, (255, 255, 255))
    screen.blit(score, [score_x, score_y])


end_font = pygame.font.Font('freesansbold.ttf', 64)
def game_over():
    end_text = end_font.render('Game Over', True, (255, 255, 255))
    screen.blit(end_text, [250, 250])

flag = True
while flag:
    screen.blit(backgroundImg,[0,0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

        # Player Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                playerX_change = 1.8
            if event.key == pygame.K_LEFT:
                playerX_change = -1.8
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    laser = mixer.Sound('Laser.wav')
                    laser.play()
                    bulletX = playerX
                    bulletFire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0 or playerX >= 836:
        playerX_change = 0
    playerShip(playerX, playerY)

    # Bullet Movement
    if bulletY <= 0:
        bullet_state = 'ready'
        bulletY = 480

    if bullet_state == 'fired':
        bulletFire(bulletX, bulletY)
        bulletY -= bulletY_change

    # Alien Movement
    for i in range(total_aliens):
        # Game Over
        if alienY[i] > 440:
            for j in range(6):
                alienY[j] = 2000
            game_over()
            break
        alienX[i] += alienX_change[i]
        if alienX[i] <= 0:
            alienX_change[i] = 1.5
            alienY[i] += alienY_change
        if alienX[i] >= 836:
            alienX_change[i] = -1.5
            alienY[i] += alienY_change

        # Collision Detection
        if isCollision(bulletX, bulletY, alienX[i], alienY[i]):
            explosion = mixer.Sound('Explosion.wav')
            explosion.play()
            bulletY = 480
            bullet_state = 'ready'
            scoreValue += 2
            alienX[i] = random.randint(0, 836)
            alienY[i] = random.randint(0, 150)

        alienShip(alienX[i], alienY[i], i)
    show_score(scoreX, scoreY)

    pygame.display.update()
pygame.quit()
