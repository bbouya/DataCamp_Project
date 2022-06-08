# Creation du board : 

from matplotlib.pyplot import grid
from sklearn.utils import column_or_1d


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


def grid_function(grid):
    # Converte grid string into a {<box> : <value>} dict with '.' value for empties
    assert len(grid) == 81, 'Input grid must be a string of lenght 81 (9*9)'

    return dict(zip(boxes, grid))

test = '..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'
le = len(test)
print(grid_function(test))