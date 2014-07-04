def checkio(game_result):
    allrows = game_result[:]
    newrows = []
    # Convert the columns into extra rows
    for i in range(3):
      for row in game_result:
        newrows.append(row[i])
    allrows.append(''.join(newrows[0:3]))
    allrows.append(''.join(newrows[3:6]))
    allrows.append(''.join(newrows[6:]))

    # Convert the diagonals into extra rows
    diagonals = [] 
    for enum, row in enumerate(game_result):
      diagonals.append(row[enum])
    for enum, row in enumerate(game_result):
      diagonals.append(row[::-1][enum])
    allrows.append(''.join(diagonals[0:3]))
    allrows.append(''.join(diagonals[3:6]))
    print allrows

    for line in allrows:
        x = 0
        o = 0
        if '.' in line:
            continue
        for i in line:
            if i == 'X':
                x += 1
                o = 0
            else:
                o += 1
                x = 0
        if x == 3:
          return "X"
        elif o == 3:
          return "O"
    return "D"
