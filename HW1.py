rows = int(input("Enter row: "))
cols = int(input("Enter col: "))

matrix = []
for x in range(rows):
    row = []
    for y in range(cols):
        row.append(float(input(f"Enter number{y+1}: ")))
    matrix.append(row)

search = float(input("Search: "))

pos = []
for x in range(rows):
    for y in range(cols):
        if matrix[x][y] == search:
            pos.append(f"Row {x}, Col {y}")

if pos:
    print(f"Number {search} found at " + " and ".join(pos) + ".")
else:
    print(f"Number {search} not found.")