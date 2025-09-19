class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows 
        self.data = {}

    def setCell(self, cell: str, value: int) -> None:
        self.data[cell] = value

    def resetCell(self, cell: str) -> None:
        if cell in self.data:
            del self.data[cell]

    def getValue(self, formula: str) -> int:
        if formula.startswith("="):
            formula = formula[1:]

        form_split = formula.split("+")
        total = 0
        for part in form_split:
            
            if part.isdigit():
                total += int(part) 
            else:
                total += self.data.get(part, 0)

        return total

                


# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)