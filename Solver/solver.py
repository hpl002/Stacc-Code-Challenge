import numpy as np
import pprint

gMarkingArr = {}

# Create random matrix.
# Specify the size and the range (range is inclusive)


def createRandomMatrix(pSize, pToInt):
    return np.random.randint(pToInt+1, size=(pSize, pSize))


# create specific matrix
# content of matrix in format: '1 1 1 1 1 ; 2 2 2 2 2 ; 3 3 3 3 3'
def createSpecificMatrix(*pNumbers):
    return np.matrix(*pNumbers)
    # handle exception


def addArrToDictionary(pDictionary, pKey, pValue):
        if pKey not in pDictionary.keys():  # create new element
                pDictionary[pKey] = [pValue]
        else:
                # get array, append new entry to array
                pDictionary[pKey].append(
                pValue)

# decode matrix into formal format
def decodeMatrix(pMatrix):
    vMatrixPositions = {}
    vCurrIndexRow = 0
    vCurrIndexElem = 0
    for row in pMatrix:
        for element in row:
                addArrToDictionary(vMatrixPositions, element, [vCurrIndexElem, vCurrIndexRow])
                vCurrIndexElem += 1
        vCurrIndexElem = 0
        vCurrIndexRow += 1
    return vMatrixPositions

# goes through each array and checks for duplicates, in effect marking down any duplicates that exist on the same row
def markHorizontalDuplicates(pDict):
        for arr in pDict.values():
                for element in arr:



 

####MAIN####
# create matrix
vTemp = createRandomMatrix(10, 10)
 
# decode matrix into dictionary
vDictionary = decodeMatrix(vTemp)
pprint.pprint(vDictionary)

# remove horizontal duplicates
markHorizontalDuplicates(vDictionary)
