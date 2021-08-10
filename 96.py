import dataclasses
import random
from typing import NoReturn


@dataclasses.dataclass(eq=True, frozen=True)
class Cell:
    row: int
    column: int
    value: int

    def __post_init__(self):
        assert (
            self.row >= 0
            and self.row <= 8
            and self.column >= 0
            and self.column <= 8
            and self.value >= 0
            and self.value <= 9
        )

    def __str__(self) -> str:
        if self.value == 0:
            return "_"

        return str(self.value)


class Grid:
    def __init__(self, cells: list[Cell]) -> None:
        self._cells = cells

    def put(self, cell: Cell, value: int) -> None:
        self._cells[self._cells.index(cell)] = dataclasses.replace(cell, value=value)

    def rows(self) -> list[list[Cell]]:
        return [self.row(r) for r in range(9)]

    def columns(self) -> list[list[Cell]]:
        return [self.column(r) for r in range(9)]

    def boxes(self) -> list[list[Cell]]:
        return [self.box(r) for r in range(9)]

    def row(self, row: int) -> list[Cell]:
        return list(filter(lambda cell: cell.row == row, self._cells))

    def column(self, column: int) -> list[Cell]:
        return list(filter(lambda cell: cell.column == column, self._cells))

    def box(self, box: int) -> list[Cell]:
        # fmt: off
        if box == 0:
            return [
                self.row(0)[0:3],
                self.row(1)[0:3],
                self.row(2)[0:3]
            ]
        elif box == 1:
            return [
                self.row(0)[3:6],
                self.row(1)[3:6],
                self.row(2)[3:6]
            ]
        elif box == 2:
            return [
                self.row(0)[6:9],
                self.row(1)[6:9],
                self.row(2)[6:9]
            ]
        elif box == 3:
            return [
                self.row(3)[0:3],
                self.row(4)[0:3],
                self.row(5)[0:3]
            ]
        elif box == 4:
            return [
                self.row(3)[3:6],
                self.row(4)[3:6],
                self.row(5)[3:6]
            ]
        elif box == 5:
            return [
                self.row(3)[6:9],
                self.row(4)[6:9],
                self.row(5)[6:9]
            ]
        elif box == 6:
            return [
                self.row(6)[0:3],
                self.row(7)[0:3],
                self.row(8)[0:3]
            ]
        elif box == 7:
            return [
                self.row(6)[3:6],
                self.row(7)[3:6],
                self.row(8)[3:6]
            ]
        elif box == 8:
            return [
                self.row(6)[6:9],
                self.row(7)[6:9],
                self.row(8)[6:9]
            ]
        # fmt: on

    def __iter__(self):
        return iter(self._cells)


class Sudoku:
    def __init__(self, grid: list[list[int]]):
        if len(grid) != 9 and len(grid[0]) != 9:
            raise ValueError("grid must be 9 by 9")

        self._pre_filled_cells = set()
        cells = []

        for i, row in enumerate(grid):
            for j, value in enumerate(row):
                cell = Cell(i, j, value)

                cells.append(cell)

                if value != 0:
                    self._pre_filled_cells.add(cell)

        self._grid = Grid(cells)

    def solve(self) -> "SolvedSudoku":
        while len(mistakes := self._check_mistakes()) != 0:
            for cell in mistakes:
                self._put(cell, random.randint(1, 9))

        return SolvedSudoku(self._grid)

    def _check_mistakes(self) -> set[Cell]:
        return set(
            [
                *self._check_row_mistakes(),
                *self._check_column_mistakes(),
                *self._check_box_mistakes(),
            ]
        )

    def _check_row_mistakes(self) -> list[Cell]:
        mistakes = []

        for row in self._grid.rows():
            seen_values = set()

            for cell in row:
                value = cell.value

                if value in seen_values:
                    mistakes.append(cell)

                seen_values.add(value)

        return mistakes

    def _check_column_mistakes(self) -> list[Cell]:
        mistakes = []

        for column in self._grid.columns():
            seen_values = set()

            for cell in column:
                value = cell.value

                if value in seen_values:
                    mistakes.append(cell)

                seen_values.add(value)

        return mistakes

    def _check_box_mistakes(self) -> list[Cell]:
        mistakes = []

        for box in self._grid.boxes():
            cells = []

            for row in box:
                for cell in row:
                    cells.append(cell)

            seen_values = set()

            for cell in cells:
                value = cell.value

                if value in seen_values:
                    mistakes.append(cell)

                seen_values.add(value)

        return mistakes

    def _put(self, cell: Cell, value: int):
        if cell in self._pre_filled_cells:
            return

        self._grid.put(cell, value)

    def __str__(self) -> str:
        rows = []

        for row in self._grid.rows():
            rows.append(" ".join(map(str, row)))

        return "\n".join(rows)

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({repr(self._grid)})"


class SolvedSudoku(Sudoku):
    def __init__(self, grid: Grid):
        self._grid = grid

    def solve(self) -> NoReturn:
        raise NotImplementedError("Can't call solve() on a solved sudoku")


def main():
    grid = [
        [0, 0, 3, 0, 2, 0, 6, 0, 0],
        [9, 0, 0, 3, 0, 5, 0, 0, 1],
        [0, 0, 1, 8, 0, 6, 4, 0, 0],
        [0, 0, 8, 1, 0, 2, 9, 0, 0],
        [7, 0, 0, 0, 0, 0, 0, 0, 8],
        [0, 0, 6, 7, 0, 8, 2, 0, 0],
        [0, 0, 2, 6, 0, 9, 5, 0, 0],
        [8, 0, 0, 2, 0, 3, 0, 0, 9],
        [0, 0, 5, 0, 1, 0, 3, 0, 0],
    ]

    sudoku = Sudoku(grid)

    print(sudoku)
    print()
    print(sudoku.solve())


if __name__ == "__main__":
    main()
