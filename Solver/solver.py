import numpy as np
import pprint

gMarkingArr=[]

# Create random matrix.
# Specify the size and the range (range is inclusive)
def createRandomMatrix(pSize, pToInt):
    return np.random.randint(pToInt+1, size=(pSize, pSize))


# create specific matrix
# content of matrix in format: '1 1 1 1 1 ; 2 2 2 2 2 ; 3 3 3 3 3'
def createSpecificMatrix(*pNumbers):
    return np.matrix(*pNumbers)
    # handle exception


# decode matrix into formal format
def decodeMatrix(pMatrix):
    vMatrixPositions = {}
    vCurrIndexRow = 0
    vCurrIndexElem = 0
    for row in pMatrix:
        for element in row:
            if element not in vMatrixPositions.keys():  # create new element
                vMatrixPositions[element] = [[vCurrIndexElem, vCurrIndexRow]]
            else:
                # get array, append new entry to array
                vMatrixPositions[element].append(
                    [vCurrIndexElem, vCurrIndexRow])
            vCurrIndexElem += 1
        vCurrIndexElem = 0
        vCurrIndexRow += 1
    return vMatrixPositions

def removeHorizontalDuplicates(pDict):
        for arr in pDict.values():
                print(arr)


 

####MAIN####
#create matrix
vTemp = createRandomMatrix(10, 10)
 
#decode matrix into dictionary
vDictionary = decodeMatrix(vTemp)
pprint.pprint(vDictionary)

#remove horizontal duplicates
removeHorizontalDuplicates(vDictionary)
