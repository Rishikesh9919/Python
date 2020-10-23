# Snake Game Development by PyGame 
import pygame, random, math

# Initializing PyGame
pygame.init()

# Screen and Icon Setup
screen_size = 500
screen = pygame.display.set_mode([screen_size, screen_size])
pygame.display.set_caption('Snake Game')
icon = pygame.image.load('Icon.png')
pygame.display.set_icon(icon)


# Background Setup
def background():
    screen.fill((0, 100, 0))
    box_size = 25
    pygame.draw.rect(screen, (0, 120, 0), [0, 0, screen_size, screen_size], 2)
    for i in range(20):
        pygame.draw.line(screen, (0, 120, 0), [0, box_size], [screen_size, box_size], 1)
        pygame.draw.line(screen, (0, 120, 0), [box_size, 0], [box_size, screen_size], 1)
        box_size += 25


# Creating Snake and Positioning It
snake_size = 25
snake_pos_x = random.randrange(0, 475, 25)
snake_pos_y = random.randrange(0, 475, 25)
snake_pos_change_x = 0
snake_pos_change_y = 0


def snake(snake_size, snake_list):
    for snake_pos in snake_list:
        pygame.draw.rect(screen, (200, 0, 0), [snake_pos[0], snake_pos[1], snake_size, snake_size], 0)


# Creating Snake Food and Giving it position
food_pos_x = random.randrange(12, 487, 25)
food_pos_y = random.randrange(12, 487, 25)


def snake_food(food_x, food_y):
    pygame.draw.circle(screen, (0, 0, 255), [food_x, food_y], 12, 0)


# After Eating food it must disappear
def eat_food(food_x, food_y, snake_pos_x, snake_pos_y):
    snake_pos_x += 12.5
    snake_pos_y += 12.5
    distance = math.sqrt(math.pow(food_x - snake_pos_x, 2) + math.pow(food_y - snake_pos_y, 2))
    if distance < 1:
        return True


# Initializing Score 
score = 0
# Snake list to append Head of snake and initial length of snake
snake_list = []
snake_length = 1

clock = pygame.time.Clock()
flag = True
while flag:
    background()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            flag = False

        # Snake Movement on click of Arrow Keys
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake_pos_change_x = -25
                snake_pos_change_y = 0
            if event.key == pygame.K_RIGHT:
                snake_pos_change_x = 25
                snake_pos_change_y = 0
            if event.key == pygame.K_UP:
                snake_pos_change_y = -25
                snake_pos_change_x = 0
            if event.key == pygame.K_DOWN:
                snake_pos_change_y = 25
                snake_pos_change_x = 0
        if event.type == pygame.KEYUP:
            snake_pos_change_x = 0
            snake_pos_change_y = 0

    # Snake food position
    snake_food(food_pos_x, food_pos_y)
    if eat_food(food_pos_x, food_pos_y, snake_pos_x, snake_pos_y):
        food_pos_x = random.randrange(12, 487, 25)
        food_pos_y = random.randrange(12, 487, 25)
        score += 1
        snake_length += 1

    # Change in movement of snake
    snake_pos_x += snake_pos_change_x
    snake_pos_y += snake_pos_change_y
    if snake_pos_x > screen_size:
        snake_pos_x = 0
    if snake_pos_x < 0:
        snake_pos_x = screen_size

    if snake_pos_y > screen_size:
        snake_pos_y = 0
    if snake_pos_y < 0:
        snake_pos_y = screen_size

    # Snake size
    snake_head = []
    snake_head.append(snake_pos_x)
    snake_head.append(snake_pos_y)
    snake_list.append(snake_head)
    if snake_length < len(snake_list):
        del snake_list[0]

    snake(snake_size, snake_list)

    # Score value
    text = pygame.font.SysFont("comicsansms", 20)
    text = text.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(text, [10, 1])

    pygame.display.update()
    clock.tick(12.5)
pygame.quit()

# End of Code
