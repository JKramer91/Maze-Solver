from window import Point, Line

class Cell:
    def __init__(self, win=None):
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True
        self.visited = False
        self._x1 = None
        self._x2 = None
        self._y1 = None
        self._y2 = None
        self._win = win
    
    def draw(self, x1, y1, x2, y2):
        if self._win is None:
            return
        
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2

        if self.has_left_wall:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x1, y2))
            self._win.draw_line(line, fill_color="white")
        if self.has_right_wall:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x2, y1), Point(x2, y2))
            self._win.draw_line(line, fill_color="white")
        if self.has_top_wall:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y1), Point(x2, y1))
            self._win.draw_line(line, fill_color="white")
        if self.has_bottom_wall:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line)
        else:
            line = Line(Point(x1, y2), Point(x2, y2))
            self._win.draw_line(line, fill_color="white")
    
    def draw_move(self, to_cell, undo=False):
        center_x1 = abs(self._x2 - self._x1) // 2 + self._x1 
        center_y1 = abs(self._y2 - self._y1) // 2 + self._y1
        center_x2 = abs(to_cell._x2 - to_cell._x1) // 2 + to_cell._x1
        center_y2 = abs(to_cell._y2 - to_cell._y1) // 2 + to_cell._y1
        
        line = Line(Point(center_x1, center_y1), Point(center_x2, center_y2))
        
        fill_color = "red"
        if undo:
            fill_color = "gray"    
        self._win.draw_line(line, fill_color=fill_color)

