from sys import exit as sys_exit
from random import sample as random_sample


class Cell:
    def __init__(self, mine=False, around_mines=0, fl_open=False):
        self.mine = mine
        self.around_mines = around_mines
        self.fl_open = fl_open


class GamePole:
    def __init__(self, n: int, m: int) -> None:
        if not (isinstance(n, int) and isinstance(m, int) and n > 1 and m > 0):
            raise ValueError("Number of cells and mines must be integers "
                             "and cells must be more than 1 "
                             "and mines more than 0")
        if m >= n * n:
            raise ValueError("Number of mines must be less "
                             "than the number of cells")
        self.n = n
        self.m = m
        self.sum_closed_cells = n * n
        self.pole = [[Cell() for _ in range(n)] for _ in range(n)]
        self.init()

    def init(self):
        all_cells = [(i, j) for i in range(self.n) for j in range(self.n)]
        mined_cells = random_sample(all_cells, self.m)
        for i, j in mined_cells:
            self.pole[i][j].mine = True
        self.sum_around_mines()

    def sum_around_mines(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.pole[i][j].mine:
                    continue
                for r, c in self.get_neighboring_cells(i, j):
                    if self.pole[r][c].mine:
                        self.pole[i][j].around_mines += 1

    def show(self):
        print("Current pole")
        for i in range(self.n):
            row = []
            for j in range(self.n):
                cell = self.pole[i][j]
                if not cell.fl_open:
                    row.append('#')
                else:
                    row.append("*" if cell.mine else str(cell.around_mines))
            print(' '.join(row))
        print("\n")

    def open_cell(self, i: int, j: int) -> None:
        try:
            cell = self.pole[i][j]
        except IndexError:
            print("Coordinates are out of range\n")
        except ValueError:
            print("Coordinates must be integers\n")
        else:
            if cell.fl_open:
                print("Cell is already open\n")
            elif cell.mine:
                self.__game_over("LOSE")
            else:
                stack = [(i, j)]
                self.open_empty_cells(stack)
                if self.sum_closed_cells == self.m:
                    self.__game_over("WIN")
                else:
                    self.show()

    def open_empty_cells(self, stack):
        while stack:
            x, y = stack.pop()
            current_cell = self.pole[x][y]
            if current_cell.fl_open:
                continue
            current_cell.fl_open = True
            self.sum_closed_cells -= 1
            if current_cell.around_mines == 0:
                for r, c in self.get_neighboring_cells(x, y):
                    if not self.pole[r][c].fl_open:
                        stack.append((r, c))

    def get_neighboring_cells(self, i, j):
        neighboring_cells = []
        for r in range(-1, 2):
            for c in range(-1, 2):
                if (
                    (r == 0 and c == 0)
                    or i + r < 0
                    or i + r >= self.n
                    or j + c < 0
                    or j + c >= self.n
                ):
                    continue
                neighboring_cells.append((i + r, j + c))
        return neighboring_cells

    def open_all_cells(self):
        for row in self.pole:
            for cell in row:
                cell.fl_open = True
        self.show()

    def __game_over(self, message):
        print(f"YOU {message}!")
        self.open_all_cells()
        sys_exit()


pole_game = GamePole(10, 12)