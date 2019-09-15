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
        vLocalDictionary={}
        for row in pMatrix:
                for element in row:
                        #check if dictionary contains element, if such
                        if element in vLocalDictionary:
                                #add index of element to existing entry
                                print()
                        else
                        vLocalDictionary[element] = row.index(element)
                                #create new entry


                 

vTemp = createRandomMatrix(10, 10)
print(vTemp)


removeHorizontalDuplicates(vTemp)

