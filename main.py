import pygame
import random
import os
import sys


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


# Основная функция
def main():
    pygame.init()
    # Создаем поле
    size = 800, 800
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Координаты клетки')

    # игровое поле 10 на 20
    board = Board(10, 20)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill('black')
        board.render(screen)
        pygame.display.flip()
    pygame.quit()


if __name__ == '__main__':
    main()