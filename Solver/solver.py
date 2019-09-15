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

  
 
#runs through matrix, removes horizontal duplicates
def removeHorizontalDuplicates(pMatrix):
    for x in np.nditer(pMatrix, flags=['external_loop'],order='C'):
        print(x)

vTemp = createRandomMatrix(10, 10)
print(vTemp)


removeHorizontalDuplicates(vTemp)

