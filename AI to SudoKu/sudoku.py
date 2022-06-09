import time
# Creation du board : 

rows = 'ABCDEFGHI'
cols = '123456789'

# Create a function that create a board 

def cross(rows, cols):
    return [r+c for r in rows for c in cols]

#print(cross(rows, cols))

# And for the units :
row_units = [cross(r, cols) for r in rows]

#print(row_units)
 
# Columns units 
col_units = [cross(rows, c) for c in cols]

#print(col_units)

# Square element : 
square_element = [cross(r,c) for r in ('ABC', 'DEF', 'GHI') for c in ('123', '456', '789')]

#print(square_element)

unitlist = row_units + col_units + square_element

# GRID FUNCTION :
boxes = cross(rows, cols)
units = dict((s, [u for u in unitlist if s in u]) for s in boxes)
peers = dict((s, set(sum(units[s], []))-set([s])) for s in boxes)



def grid_function(grid):
    # Converte grid string into a {<box> : <value>} dict with '.' value for empties
    assert len(grid) == 81, 'Input grid must be a string of lenght 81 (9*9)'

    return dict(zip(boxes, grid))

test = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
le = len(test)
#print(grid_function(test))

# Display the grid 
def display(values):
    width = 1+max(len(values[s]) for s in boxes)
    line = '+'.join(['-'*(width*3)]*3)

    for r in rows:
        print(''.join(['-'*(width*3)])*3)
        for r in rows:
            print(''.join(values[r+c].center(width)+('|' if c in '36' else '') for c in cols))
            if r in 'CF': print(line)
        return



# gird values function if its empty put (1.2.3.4.5.6.7.8.9) if not let the number

def grid_values(grid):
    """
    convert grid string into {box:value} dict with '123456789' for the empties.
    """
    values = []
    all_digits = '123456879'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
        
    assert len(values) == 81
    return dict(zip(boxes, values))

#print(grid_values(test))

print(display(grid_values(test)))

# Implementation eliminate :
def eliminate(values):
    """
    Eliminate values from peers of each box with a single values.

    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]

    for box in solved_values:
        digit = values[box]
        for peer in peers[box]:
            values[peer] = values[peer].replace(digit, '')
            print(display(values))
            time.sleep(0.1)

    return values
#print(eliminate(grid_values(test)))
#print(display(eliminate(grid_values(test))))

print(peers["A1"])
print(units["A1"])
print(square_element[0])