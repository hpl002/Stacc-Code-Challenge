import numpy as np
import pprint
gMatrixLength = 0
gMatrixMaxInt = 0
gMarkingDict_Horizontal = {}
gMarkingDict_Vertical = {}
# Create random matrix.
# Specify the size and the range (range is inclusive)


def createRandomMatrix(pSize, pToInt):
    return np.random.randint(pToInt+1, size=(pSize, pSize))


# create specific matrix
def createSpecificMatrix(*pArgs):
        vReturn = []
        for arg in pArgs:
                vTemp = []
                vList = arg.split (",")
                for e in vList:
                        vTemp.append(int(e))
                vReturn.append(vTemp)
        return np.array(vReturn)


def addArrToDictionary(pDictionary, pKey, pValue):
        if pKey not in pDictionary.keys():  # create new element
                pDictionary[pKey] = [pValue]
        else:
                # get array, append new entry to array
                if pValue not in pDictionary[pKey]:
                        pDictionary[pKey].append(
                        pValue)

# decode matrix into formal format
def decodeMatrix(pMatrix):
        global gMatrixLength
        global gMatrixMaxInt
        gMatrixLength = pMatrix.shape[0]
        vMatrixPositions = {}
        vCurrIndexRow = 0
        vCurrIndexElem = 0
        for row in pMatrix:
                for element in row:
                        addArrToDictionary(vMatrixPositions, element, [vCurrIndexElem, vCurrIndexRow])
                        if element > gMatrixMaxInt:
                                gMatrixMaxInt = element
                        vCurrIndexElem += 1
                vCurrIndexElem = 0
                vCurrIndexRow += 1
        return vMatrixPositions

# goes through each array and checks for duplicates, in effect marking down any duplicates that exist on the same row
#increases int such that we do not seach unneccesarily
def markHorizontalDuplicates(pDict):
          for i in range(gMatrixMaxInt+1):
                if i in pDict:
                        vCurrArr = pDict[i]
                        skip = 0
                        for element in vCurrArr:
                                vAddedCurrentElem = False
                                for e in vCurrArr[skip:]:                                
                                        if element[1]  == e[1]:
                                                if element != e and not vAddedCurrentElem:
                                                        addArrToDictionary(gMarkingDict_Horizontal, i, element)
                                                        addArrToDictionary(gMarkingDict_Horizontal, i, e)
                                                        vAddedCurrentElem = True
                                                elif element != e:
                                                        addArrToDictionary(gMarkingDict_Horizontal, i, e)
                                skip+=1

#When looking for duplicates in the vertical axis we look at the X value
def markVerticalDuplicates(pDict):
          for i in range(gMatrixMaxInt+1):
                if i in pDict:
                        vCurrArr = pDict[i]
                        for element in vCurrArr:
                                vAddedCurrentElem = False
                                for e in vCurrArr:      
                                        if element[0]  == e[0]:
                                                if element != e and not vAddedCurrentElem:
                                                        addArrToDictionary(gMarkingDict_Vertical, i, element)
                                                        addArrToDictionary(gMarkingDict_Vertical, i, e)
                                                        vAddedCurrentElem = True
                                                elif element != e:
                                                        addArrToDictionary(gMarkingDict_Vertical, i, e)
#helper that gets the dictionary key associated with a certain value
def getKeyWithValue(pDict, value):
        for i in range(gMatrixMaxInt+1):
                if i in pDict:
                        if(value in pDict[i]):
                                return i
                        i+=1
 
def solver(pDict):
        vResult = []
        #This var is in essence the length and width of the grid
        for y in range(gMatrixLength):
                for x in range(gMatrixLength):
                        vResult.append(getKeyWithValue(pDict, [x,y]))
        return vResult


#MAIN - Insturctions
# Either create a matrix by passing in numbers or generate one of any size
# Create the dictionaries that hold the horizontal and vertical duplicates
# run the solver on the dictioanry created from the matrix. The solver uses the marking dictionaries, it is therefore paramoutn that these are run beforehand 
def Main():
        vMatrix = createRandomMatrix(10, 10)
        vMatrix = createSpecificMatrix('5, 2, 1, 6, 2, 5', '3, 1, 4, 2, 6, 6', '4, 2, 3, 4, 6, 3', '4, 5, 6, 3 ,2, 2', '2, 4, 3, 3, 4, 5', '6, 4, 6, 5, 3, 3')
        #vMatrix = np.array([[5, 2, 1, 6, 2, 5],[3, 1, 4, 2, 6, 6], [4, 2, 3, 4, 6, 3], [4, 5, 6, 3 ,2, 2], [2, 4, 3, 3, 4, 5], [6, 4, 6, 5, 3, 3]])
        print(vMatrix)
        vDictionary = decodeMatrix(vMatrix)
        markHorizontalDuplicates(vDictionary)
        markVerticalDuplicates(vDictionary)
        print(solver(vDictionary))

Main()
 
         
 