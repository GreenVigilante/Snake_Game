import pygame
import random
pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 128, 0)

width, height = 1280, 720

game_display = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake game")
snake_speed = 20
snake_size = 20
clock = pygame.time.Clock()

message_font = pygame.font.SysFont('ubuntu', 30)
score_font = pygame.font.SysFont('ubuntu', 20)
highest_score = []
def draw_snake(snake_size, snake_pixels):
    for pixel in snake_pixels:
        pygame.draw.rect(game_display, green, [pixel[0], pixel[1], snake_size, snake_size])
def print_score(score):
    text_score = score_font.render(f"Score: {str(score)}",True, white)
    game_display.blit(text_score, [0,0])

def game_run():
    game_over = False
    game_close = False
    x = width/2
    y= height/2
    x_speed = 0
    y_speed = 0
    snake_length = 1
    snake_pixels = []
    
    target_x= round(random.randrange(0, width-snake_size)/snake_size)*snake_size
    target_y= round(random.randrange(0, height-snake_size)/snake_size)*snake_size
    
    while not game_close:
        while game_over:
            highest_score.append(snake_length-1)
            game_over_mess = message_font.render("Game Over!", True , red)
            text = message_font.render("Enter 0 to exit or 1 to play again", True, white)
            high_text = message_font.render(f"Your highest score is {max(highest_score)}", True, white)
            game_display.blit(game_over_mess, [width/3,height/3])
            game_display.blit(text, [width/2, height/2])
            game_display.blit(high_text, [width/1.5, height/1.5])
            print_score(snake_length-1)
            pygame.display.update()
            x = width/2
            y= height/2
            x_speed = 0
            y_speed = 0
            snake_length = 1
            snake_pixels = []
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_0:
                        game_close = True
                        game_over = False
                    elif event.key ==pygame.K_1:
                        game_over = False
        for event in pygame.event.get():
            if event.type== pygame.QUIT:
                game_close = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_speed = -snake_size
                    y_speed = 0
                if event.key == pygame.K_RIGHT:
                    x_speed = snake_size
                    y_speed = 0
                if event.key == pygame.K_UP:
                    x_speed = 0
                    y_speed = -snake_size
                if event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = snake_size
        if x>width  or y>height  or x<0 or y<0:
            game_over = True
        x = x+x_speed
        y = y+y_speed
        game_display.fill(black)
        pygame.draw.rect(game_display, red, [target_x, target_y, snake_size, snake_size])
        snake_pixels.append([x,y])

        if len(snake_pixels)>snake_length:
            del snake_pixels[0]
        
        for pixel in snake_pixels[:-1]:
            if pixel == [x,y]:
                game_over = True
        draw_snake(snake_size, snake_pixels)
        print_score(snake_length-1)
        pygame.display.update()
        if x==target_x and y==target_y:
            target_x= round(random.randrange(0, width-snake_size)/snake_size)*snake_size
            target_y= round(random.randrange(0, height-snake_size)/snake_size)*snake_size
            snake_length = snake_length +1
        clock.tick(snake_speed)
        
    pygame.quit
    quit()
game_run()
