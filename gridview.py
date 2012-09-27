#A Gridview Class

import pygame
from pygame.locals import *


class GridView(object):
        """
        A Gridview Class
        """
        def __init__(self, surface, width, height, grid_size, grid_color,
                     grid_width=1):
                """ initalize the grid view
                x_grid_num: the horizontal grid number(width/grid_size)
                y_grid_num: the vertical grid number(heigth/grid_size)
                """
                if (width % grid_size != 0
                    or height % grid_size != 0):
                        raise CanNotDivideException(
                            'the grid_size is not suitable for width and height'
                        )

                self.x_grid_num = width / grid_size
                self.y_grid_num = height / grid_size

                self.surface = surface
                self.width = width
                self.height = height
                self.grid_size = grid_size
                self.grid_color = grid_color
                self.grid_width = grid_width

        def draw(self):
                """
                draw the grid
                """
                for y in range(0, self.height, self.grid_size):
                        for x in range(0, self.width, self.grid_size):
                                pygame.draw.rect(self.surface, self.grid_color, 
                                                 ((x, y), (self.grid_size, self.grid_size)), self.grid_width)

        def fill_a_cell(self, x, y, color):
                """
                fill a cell in the grid view
                x, y: the coordinate in the grid_view
                x: the column number
                y: the row number
                """
                if x > self.x_grid_num or y > self.y_grid_num or x < 0 or y < 0:
                        raise CoordinateTooBigException('the x y coordinate is error' + \
                                                       'x = ' + str(x) +
                                                        ', y = ' + str(y))
                
                pygame.draw.rect(self.surface, color, ((x*self.grid_size, y*self.grid_size), 
                                                       (self.grid_size, self.grid_size)), 0)

        def fill_a_cell_with_circle(self, x, y, color):
                """
                fill a cell with circle in the grid
                x, y: the coordinate in the grid_view
                x: the column number
                y: the row number
                """
                if x > self.x_grid_num or y > self.y_grid_num or x < 0 or y < 0:
                        raise CoordinateTooBigException('the x y coordinate is error')

                delta = self.grid_size // 2
                pygame.draw.circle(self.surface, color, (x * self.grid_size + delta, y * self.grid_size + delta),
                                   delta - 2, 0)

        def draw_array_in_grid(self, array, draw_color, special_pos=None,
                               special_color=None):
            """
            draw this array in the center-bottom of grid
            """
            width = self.x_grid_num
            height = self.y_grid_num
            array_size = len(array)
            if array_size > width:
                raise ArrayToLongError("The array size " + str(array_size) +
                                      " is too big")
            else:
                # start draw the array in grid
                cur_pos = (width - array_size) / 2
                cur_index = 0
                for num in array:
                    if special_color and special_pos \
                        and special_pos == cur_index:
                        for i in xrange(num):
                            # draw from bottom
                            self.fill_a_cell(cur_pos, height - 1 - i,
                                             special_color)
                    else:
                        for i in xrange(num):
                            # draw from bottom
                            self.fill_a_cell(cur_pos, height - 1 - i,
                                             draw_color)
                    cur_index += 1
                    cur_pos += 1


class CoordinateTooBigException(BaseException):
        def __init__(self, description):
                self.description = description

        def __unicode__(self):
                return 'error: ' + str(self.description)


class CanNotDivideException(BaseException):
        def __init__(self, description):
                self.description = description

        def __repr__(self):
                return 'error: ' + str(description)

        def __unicode__(self):
                return self.__repr__()


class ArrayToLongError(BaseException):
        def __init__(self, description):
                self.description = description

        def __unicode__(self):
                return 'error: ' + str(self.description)
