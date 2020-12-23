import pygame
from random import randint
import os
import sys


BOX = {1: [[[0, 0], [1, 0], [1, 1], [0, 1]]]}

pygame.init()


class Board:
    # создание поля
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * width for _ in range(height)]
        # значения по умолчанию
        self.left = 20
        self.top = 0
        self.cell_size = 40

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, pygame.Color(255, 255, 255), (
                    x * self.cell_size + self.left, y * self.cell_size + self.top, self.cell_size,
                    self.cell_size), 1)


class Figure:
    def __init__(self, screen, type_figure, color, x, y, box, turn):
        self.screen = screen
        self.box = box
        self.turn = turn
        self.x = x * 40 + 20
        self.y = y * 40
        self.type_figure = type_figure
        self.color = color
        self.w, self.h = 40, 40

    def render(self):
        for i in self.box[self.type_figure][self.turn]:
            pygame.draw.rect(self.screen, self.color, (self.x + i[0] * 40, self.y + i[1] * 40, self.w, self.h))


# Основная функция
def main():
    pygame.init()
    # Создаем поле
    size = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Tetris')

    # игровое поле 10 на 20
    board = Board(10, 20)
    # новая фигура
    new_figure = True

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('black')
        board.render(screen)

        if new_figure:
            f = Figure(screen, 1, 'yellow', 4, 0, BOX, 0)
            f.render()

        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()