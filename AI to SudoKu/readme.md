# Applaying AI on Sudoku Game:

Sudoku : Solution
The solution probably consisted of the following two steps () : 
    - if a box has a value, the, all the boxes in the same row, same column, or same 3*3 square cannot have that same value.
    - if there is only one allowed value for a given box in a row, column, or 3*3 square, then the box is assigned that value.
# Naming Conventions :
Since we are writing an agent to solve : 
    - The rows will be labelled the letters A, B, C, D, E, F, G, H, I.
    - The columns will be labelled by the numbers 1, 2, 3, 4, 5, 6, 7, 8, 9.
    Here we can see the unsolved and solved puzzle with the labels for the rows and columns.
    - The 3*3 squares won't be labeled, but in the diagram, they can be seen with alternating colors of grey and white.

# Boxes, Units and peers 
    - The individual squares at the intersection of rows and columns will be called boxes. these boxes will have labels 'A1', A2, ..... , 'I9.

# Creation du sudoku.py : 
Now, in order to implement an agent, let's start by coding the board in python, Then, we will code the necessary functions to solve the sudoku;
We will record the puzzles in two ways - as a string and as a dictionary.
The string will consist of a concatenation of all the readings of the digits in the rows, taking the rows from top to bottom, If the puzzle is not solved, we can use a (.) as a placec holder for an empty box.

# function GRID_Values() :
A function to convert the string representation of a puzzle into a dictionary form.
