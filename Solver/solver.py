import numpy as np


#Create random matrix.
#Specify the size and the range (range is inclusive)
def createRandomMatrix(pSize, pToInt):
    return  np.random.randint(pToInt+1, size=(pSize, pSize))


#create specific matrix
#content of matrix in format: '1 1 1 1 1 ; 2 2 2 2 2 ; 3 3 3 3 3'
def createSpecificMatrix(*pNumbers):
    return np.matrix(*pNumbers)
    #handle exception

  
 
#decode matrix into formal format
def decodeMatrix(pMatrix):
        vMatrixPositions={}
        vCurrIndexRow = 0
        vCurrIndexElem = 0
        for row in pMatrix:
                vCurrIndexRow+=1
                for element in row:
                        vCurrIndexElem+=1
                        if element not in vMatrixPositions.keys(): #create new element
                                vMatrixPositions[element] = 300
                                

                         

 

                 

vTemp = createRandomMatrix(10, 10)
print(vTemp)

 
