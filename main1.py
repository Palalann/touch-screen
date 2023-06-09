# Declare a 2-D array used for screen.
# This 2-D array could be written in the form of screen[column, row]
# where column is the number of vertical pixels and row is number of horizontal pixels
screen = [[column for column in range(1280)]for row in range(4)]
# Procedure setRow will set a required number of pixels to 1.
# setRow(row number, number of pixels skipped starting from column1, number of pixel that should set to 1)
# For example setRow(1, 2, 3) will set row 1, column 2 and set 3 pixels to 1
# Use to generate test data.
def setRow(self,row, skipN, setN) :
    self.skipN = skipN
    self.setN = setN
    self.row = row


    for column in [skipN+1, setN + skipN] :
        screen[row][column] = 1

# Function searchInRow(row number, start column)
# Searches the given row from the start column (either left to right or right to left)
# for the first column that contains an element set to 1
def searchInRow(self, thisRow, startColumn) :
    self.thisRow = thisRow
    self.startColumn = startColumn
    found = False
    thisColumn = startColumn
    if startColumn == 1 :
        step = 1
        endColumn = 1281
    else :
        step = -1
        endColumn = 0
    while thisColumn != endColumn and found == False :
        if screen[thisRow][thisColumn] != 1 :
            thisColumn += step
        else :
            found == True

    if found == False :
        thisColumn = -1

    return thisColumn

# Function searchInCol(column number, start row)
# Searches the given column from the start row (either up or down) for the first
# row that contains an element set to 1
# Same as the function above
def searchInCol(self, thisCol, startRow) :
    self.thisCol = thisCol
    self.startRow = startRow
    found = False
    thisRow = startRow
    if startRow == 1 :
        step = 1
        endRow = 1281
    else :
        step = -1
        endRow = 0
    while thisRow != endRow and found == False :
        if screen[thisCol][thisRow] != 1 :
            thisRow += step
        else :
            found == True

    if found == False :
        thisRow = -1

    return thisRow

#Function getCentreCol(row number)
#Use searchInRow() to find first and last columns in the given row which have array element set to 1
#Returns the index of the column midway between the first and last columms
#If no element is set to 1, returns -1
def getCentreColumn(self, thisRow) :
    self.thisRow = thisRow
    startColumn = searchInRow(thisRow, 1)
    if startColumn == -1 :
        centreColumn = startColumn
    else :
        endColumn = searchInRow(thisRow, 1280)
        centreColumn = int((startColumn + endColumn)/2)
    return centreColumn

def getCentreRow(self, thisColumn) :
    self.thisColumn = thisColumn
    startRow = searchInColumn(thisColumn, 1)
    if startRow == -1 :
        centreRow = startRow
    else :
        endRow = searchInColumn(thisColumn, 1280)
        centreRow = int((startRow + endRow)/2)
    return centreRow