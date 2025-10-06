rows = [0] * 40
columns = [0] * 30
for rowNum in range(0, len(rows)):
    toAddToCol = []
    for colNum in range(0, len(columns)):
        toAddToCol.append(float(input(">")))
    columns[rowNum] = toAddToCol

for colsToDo in rows:
    print(sum(colsToDo))
