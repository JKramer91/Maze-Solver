from window import Window, Point, Line
from cell import Cell
from maze import Maze

def main():
    screen_x = 800
    screen_y = 600
    num_rows = 12
    num_cols = 16
    margin = 50
    cell_size_x = 40
    cell_size_y = 40
    win = Window(screen_x, screen_y)
    maze = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    win.wait_for_close()

main()