from typing import List


class Bingo:
    def __init__(self, numbers: List[str]):
        self.rows = self._make_rows(numbers)
        self.checked_rows = [[False for __ in range(5)] for _ in range(5)]

    def _make_rows(self, numbers: List[str]) -> List[List[int]]:
        fixed_numbers = [line.replace("  ", " ").strip() for line in numbers]
        rows = [[int(i) for i in line.split(" ")] for line in fixed_numbers]
        return rows

    def check(self, number: int):
        for irow, row in enumerate(self.rows):
            for inum, num in enumerate(row):
                if num == number:
                    self.checked_rows[irow][inum] = True
                    break

        if self.is_row_bingo() or self.is_col_bingo():
            print(self.rows)
            print(self.checked_rows)
            not_checked = sum(
                self.rows[row][col] for row in range(5) for col in range(5) if not self.checked_rows[row][col])
            return not_checked * number

    def is_row_bingo(self) -> bool:
        return any(all(row) for row in self.checked_rows)

    def is_col_bingo(self) -> bool:
        return any(all(row[i] for row in self.checked_rows) for i in range(5))


def part1(lines: List[str]) -> int:
    called_line, _, *rest = lines
    called = called_line.split(",")

    cards = []
    for i in range(0, len(rest), 6):
        card_lines = rest[i:i + 5]
        bingo_card = Bingo(card_lines)
        cards.append(bingo_card)
    print(f"got {len(cards)} cards")

    for number in called:
        print(f"calling number {number}")
        for card in cards:
            bingo = card.check(int(number))
            if bingo:
                print("BINGO!")
                return bingo


def part2(lines: List[str]) -> int:
    called_line, _, *rest = lines
    called = called_line.split(",")

    cards = []
    for i in range(0, len(rest), 6):
        card_lines = rest[i:i + 5]
        bingo_card = Bingo(card_lines)
        cards.append(bingo_card)
    print(f"got {len(cards)} cards")

    for number in called:
        print(f"calling number {number}")
        remaining_cards = []
        for card in cards:
            bingo = card.check(int(number))
            if not bingo:
                remaining_cards.append(card)
        if not remaining_cards:
            return bingo
        cards = remaining_cards
