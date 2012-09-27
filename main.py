from gridview import GridView
from pygame.locals import *
from sortalg import SortAlg

from sys import exit

import pygame


width = 765
height = 615
grid_size = 15
# x_num=51, y_num=41
resolution = (width, height)
background_color = (230, 230, 100)
grid_line_color = (0, 0, 0)
cell_color = (50, 50, 255)
special_cell_color = (255, 50, 50)
array_size = 41


def main(speed=0.1):
    screen = pygame.display.set_mode(resolution, 0, 32)
    clock = pygame.time.Clock()
    grid_view = GridView(screen, width, height, grid_size, grid_line_color)

    sort_alg = SortAlg(array_size)
    sort_alg.generate_random_array()
    #path_track = sort_alg.bubble_sort()
    path_track = sort_alg.select_sort()
    #path_track = sort_alg.insert_sort()
    print path_track

    # some utility variable
    index = 0
    pass_time = 0

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()

        screen.fill(background_color)

        grid_view.draw_array_in_grid(path_track[index][0], cell_color,
                                     path_track[index][1], special_cell_color)

        grid_view.draw()
        time_passed_second = clock.tick() / 1000.0
        pass_time += time_passed_second

        if pass_time >= speed:
            pass_time = 0
            index = index + 1
            if index >= len(path_track):
                index = len(path_track) - 1

        pygame.display.update()


if __name__ == '__main__':
    pygame.init()
    main()
