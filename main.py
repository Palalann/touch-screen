screen = [[column for column in range(1280)]for row in range(4)]
def setRow(self,row, skipN, setN) :
    self.skipN = skipN
    self.setN = setN
    self.row = row


    for column in [skipN+1, setN + skipN] :
        screen[row][column] = 1


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

def getCentreColumn(self, thisRow) :
    self.thisRow = thisRow
    startColumn = searchInRow(thisRow, 1)
    if startColumn == -1 :
        centreColumn = startColumn
    else :
        endColumn = searchInRow(thisRow, 1280)
        centreColumn = int((startColumn + endColumn)/2)
    return centreColumn

