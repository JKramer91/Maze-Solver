import time
import random
from cell import Cell

class Maze:
    def __init__(self, x1, y1, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []
        if seed is not None:
            random.seed(seed)
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0,0)
        self._reset_cells_visited()

    def _create_cells(self):
        self._cells = [[Cell(self._win) for j in range(self._num_rows)] for i in range(self._num_cols)]

        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self._win is None:
            return
        
        x1 = self._x1 + i * self._cell_size_x
        y1 = self._y1 + j * self._cell_size_y
        x2 = x1 + self._cell_size_x
        y2 = y1 + self._cell_size_y

        self._cells[i][j].draw(x1, y1, x2, y2)

        self._animate()
    
    def _animate(self):
        if self._win is None:
            return
        
        self._win.redraw()
        time.sleep(0.03)
    
    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        i = self._num_cols - 1
        j = self._num_rows - 1
        self._cells[i][j].has_bottom_wall = False
        self._draw_cell(i, j)
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True
        
        while True:
            adjacent = []

            # left
            if i > 0 and not self._cells[i - 1][j].visited:
                adjacent.append((i - 1, j))
            # right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                adjacent.append((i + 1, j))
            # up
            if j > 0 and not self._cells[i][j - 1].visited:
                adjacent.append((i, j - 1))
            # down
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                adjacent.append((i, j + 1))

            if not adjacent:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(adjacent))
            next_i, next_j = adjacent[direction_index]

            # right
            if next_i == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            # left
            if next_i == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            # down
            if next_j == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            # up
            if next_j == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False

            self._break_walls_r(next_i, next_j)
    
    def _reset_cells_visited(self):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
    
    def _solve_r(self, i, j):
        self._animate()

        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True
        
        curr = self._cells[i][j]
        # left
        if i > 0 and not self._cells[i - 1][j].visited and not curr.has_left_wall:
            curr.draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                curr.draw_move(self._cells[i - 1][j], True)
        # right
        if i < self._num_cols - 1 and not self._cells[i + 1][j].visited and not curr.has_right_wall:
            curr.draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                curr.draw_move(self._cells[i + 1][j], True)
        # up
        if j > 0 and not self._cells[i][j - 1].visited and not curr.has_top_wall:
            curr.draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                curr.draw_move(self._cells[i][j - 1], True)
        # down
        if j < self._num_rows - 1 and not self._cells[i][j + 1].visited and not curr.has_bottom_wall:
            curr.draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                curr.draw_move(self._cells[i][j + 1], undo=True)

        return False
    
    def solve(self):
        return self._solve_r(0, 0)