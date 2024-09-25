import random
import sys
import pygame
from pygame import Vector2
import random

pygame.init()
title_font = pygame.font.Font(None , 40)
score_font = pygame.font.Font(None , 30)
green = (173 , 204 , 96)
dark_green = (43 , 51 , 24)
cell_size = 25
no_of_cells = 26
class  Food():
    def __init__(self):
        self.position = Vector2(random.randint(0 , cell_size -1),random.randint(0 , cell_size -1))
    def draw(self):
        screen_surface = pygame.Rect(self.position.x * cell_size , self.position.y * cell_size , cell_size , cell_size )
        pygame.draw.rect(screen , dark_green , screen_surface , 0 ,16)


class Snake():
    def __init__(self):
        self.body = [Vector2(5,9) , Vector2(6,9) , Vector2(7,9)]
        self.direction = Vector2(1,0)
        self.add_segment = False



    def draw(self):
        for segments in self.body:
            snake_surface = pygame.Rect(segments[0] * cell_size , segments[1] * cell_size , cell_size ,cell_size )
            pygame.draw.rect(screen , dark_green , snake_surface , 0 , 8)

    def update(self):

        self.body.insert(0 , self.body[0] + self.direction)
        if self.add_segment == True:
            self.add_segment = False
        else:
            self.body = self.body[:-1]
    def reset_snake(self):
        self.body = [Vector2(5,9) , Vector2(5,9) , Vector2(5,9)]
        self.direction = Vector2(1 ,0)


class Game():
    def __init__(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def draw(self):
        self.food.draw()
        self.snake.draw()
    def update(self):
        self.snake.update()
        self.check_collision_food()
        self.check_collision_edges()
        self.check_collision_itsels()


    def check_collision_food(self):
        if self.snake.body[0] == self.food.position:
            self.food.position = Vector2(random.randint(0 , cell_size -1),random.randint(0 , cell_size -1))
            self.snake.add_segment = True
            self.score = self.score +1


    def check_collision_edges(self):
        if self.snake.body[0].x ==  26 or self.snake.body[0].x == -1:
            self.snake.reset_snake()
        if self.snake.body[0].y ==  no_of_cells or self.snake.body[0].y == -1:
            self.snake.reset_snake()
            self.score = 0


    def check_collision_itsels(self):
        if self.snake.body[0] in  self.snake.body[1:]:
            self.snake.reset_snake()
            self.score = 0




screen = pygame.display.set_mode((650, 650))
pygame.display.set_caption('snake game')


clock = pygame.time.Clock()

game = Game()
SNAKE_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SNAKE_UPDATE , 200)
while True:
    for event in pygame.event.get():
        if event.type == SNAKE_UPDATE:

            game.update()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and game.snake.direction != Vector2(0,1):
                game.snake.direction = Vector2(0,-1)
            if event.key == pygame.K_DOWN and game.snake.direction != Vector2(0,-1):
                game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_LEFT and game.snake.direction != Vector2(1,0):
                game.snake.direction = Vector2 (-1,0)
            if event.key == pygame.K_RIGHT and game.snake.direction != Vector2(-1,0):
                game.snake.direction = Vector2(1,0)



    screen.fill(green)
    game.draw()
    title_surface = title_font.render('Sanp wali Game' , True , dark_green)
    screen.blit(title_surface , (5 , 20))
    score_surface = title_font.render( str(game.score), True, dark_green)
    screen.blit(score_surface, (1, 570))
    pygame.display.update()
    clock.tick(60)
