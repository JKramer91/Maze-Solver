import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1._cells),
            num_cols,
        )
        self.assertEqual(
            len(m1._cells[0]),
            num_rows,
        )
    
    def test_maze_cell_size(self):
        cell_size_x = 30
        cell_size_y = 25
        m1 = Maze(0, 0, 12, 10, cell_size_x, cell_size_y)
        self.assertEqual(
            m1._cell_size_x,
            cell_size_x
        )
        
        self.assertEqual(
            m1._cell_size_y,
            cell_size_y
        )
    
    def test_maze_break_entrance_and_exit(self):
        m1 = Maze(0, 0, 12, 10, 20, 20)
        m1._break_entrance_and_exit()

        self.assertEqual(
            m1._cells[0][0].has_top_wall,
            False
        )

        self.assertEqual(
            m1._cells[m1._num_cols - 1][m1._num_rows - 1].has_bottom_wall,
            False
        )

    def test_maze_reset_cells_visited(self):
        m1 = Maze(5, 5, 12, 10, 8, 8)
        for col in m1._cells:
            for cell in col:
                self.assertEqual(
                    cell._visited,
                    False
                )



if __name__ == "__main__":
    unittest.main()