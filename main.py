from window import Window, Point, Line
from cell import Cell

win = Window(800, 600)
c1 = Cell(win)
c1.draw(10, 10, 50, 50)
c2 = Cell(win)
c2.has_right_wall = False
c2.draw(50, 50, 90, 90)
win.wait_for_close()