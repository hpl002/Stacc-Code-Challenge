import numpy as np
import pprint

gMarkingDict = {}

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
#increases int such that we do not seach unneccesarily
def markHorizontalDuplicates(pDict):
          for i in range(len(pDict)):
                vCurrArr = pDict[i]
                skip = 0
                for element in vCurrArr:
                        yPosition = element[1] 
                        for e in vCurrArr[skip:]:                                
                                if yPosition == e[1]:
                                        addArrToDictionary(gMarkingDict, i, element)
                        skip+=1



#[[5, 2], [9, 2], [6, 6], [0, 7], [5, 8], [7, 9]],




 

####MAIN####
# create matrix
#vTemp = createRandomMatrix(10, 10)
#print(vTemp)
# decode matrix into dictionary
vDictionary = {0: [[4, 0],
     [5, 0],
     [6, 0],
     [5, 1],
     [1, 3],
     [4, 4],
     [4, 5],
     [1, 6],
     [0, 7],
     [6, 7],
     [5, 8],
     [9, 8],
     [1, 9],
     [8, 9],
     [9, 9]],
 1: [[3, 2], [6, 3], [9, 4], [5, 5], [6, 5], [0, 8]],
 2: [[8, 0],
     [0, 1],
     [3, 1],
     [3, 4],
     [2, 6],
     [2, 7],
     [5, 7],
     [3, 8],
     [8, 8],
     [2, 9],
     [3, 9]],
 3: [[2, 0],
     [6, 1],
     [1, 2],
     [4, 2],
     [5, 2],
     [2, 3],
     [5, 4],
     [8, 4],
     [6, 8],
     [6, 9]],
 4: [[1, 0], [2, 1], [9, 5], [8, 7], [2, 8], [7, 8]],
 5: [[7, 1], [8, 1], [2, 4], [4, 6], [7, 6], [7, 7], [1, 8], [7, 9]],
 6: [[4, 1], [3, 3], [1, 7], [0, 9], [4, 9], [5, 9]],
 7: [[9, 0],
     [6, 2],
     [7, 2],
     [9, 2],
     [8, 3],
     [9, 3],
     [1, 4],
     [2, 5],
     [3, 5],
     [9, 6]],
 8: [[3, 0],
     [7, 0],
     [9, 1],
     [0, 2],
     [7, 3],
     [0, 5],
     [7, 5],
     [5, 6],
     [6, 6],
     [4, 8]],
 9: [[0, 0], [8, 2], [0, 4], [0, 6], [3, 6], [4, 7], [9, 7]],
 10: [[1, 1],
      [2, 2],
      [0, 3],
      [4, 3],
      [5, 3],
      [6, 4],
      [7, 4],
      [1, 5],
      [8, 5],
      [8, 6],
      [3, 7]]}
  
# remove horizontal duplicates
markHorizontalDuplicates(vDictionary)
pprint.pprint(vDictionary)
print('separator')
pprint.pprint(gMarkingDict)


 
         
 