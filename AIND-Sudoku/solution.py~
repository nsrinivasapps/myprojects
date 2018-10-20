assignments = []
rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [x + y for x in A for y in B]

boxes = cross(rows,cols)
rowUnits = [cross(r,cols) for r in rows]
colUnits =  [cross(rows,c) for c in cols]
sqUnits = [cross(r,c) for r in ('ABC','DEF','GHI') for c in ('123','456','789')]
# diagonal units of a sudoku
diagUnits = [[x+y for x, y in zip(rows, cols)], [x+y for x, y in zip(rows, cols[::-1])]]
unitList = rowUnits + colUnits + sqUnits + diagUnits

units = dict((s,[u for u in unitList if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in boxes)

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    naked_twin_dict = {}
    for unit in unitList:
        uDict = {}
        for box in unit:
            if len(values[box]) == 2:
               if not values[box] in uDict:
                  uDict[values[box]] = [box]
               else:
                  uDict[values[box]].append(box) 
        for key in uDict:            
            if len(uDict[key]) == 2:
                if not key in naked_twin_dict:
                    naked_twin_dict[key] = [unit]
                else:
                    naked_twin_dict[key].append(unit)
                
    # Eliminate the naked twins as possibilities for their peers
    for key in naked_twin_dict:
        for unit in naked_twin_dict[key]:
            for box in unit:
                if values[box] != key:
                    assign_value(values, box, values[box].replace(key[0], ''))
                    assign_value(values, box, values[box].replace(key[1], ''))
    return values
    

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    chars = []
    for c in grid:
        if c in cols:
           chars.append(c)
        elif c in '.0':
           chars.append(cols)
    assert len(chars) == 81
    return dict(zip(boxes,chars))
    

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit,'')
    return values

def only_choice(values):
    for unit in unitList:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values

def reduce_puzzle(values):
    stalled = False
    while not stalled:
       solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
       values = eliminate(values)
       values = naked_twins(values)
       values = only_choice(values)
       solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
       stalled = solved_values_before == solved_values_after
       if len([box for box in values.keys() if len(values[box]) == 0]):
          return False
    return values

def search(values):    
    values = reduce_puzzle(values)
    if values is False:
       return False
    if all(len(values[s]) == 1 for s in boxes):
       return values

    n,s = min((len(values[s]),s) for s in boxes if len(values[s]) > 1)

    for value in values[s]:
        new_suduko = values.copy()
        new_suduko[s] = value
        attempt = search(new_suduko)
        if attempt:
           return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    values = grid_values(grid)
    values = search(values)
    return values
    

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
