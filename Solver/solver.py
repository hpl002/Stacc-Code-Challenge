import numpy as np
import pprint
import random
from collections import Counter
gMatrixLength = 0
gMatrixMaxInt = 0
gMarkingDict_Horizontal = {}
gMarkingDict_Vertical = {}
#dictionary containing the positions of the entries that are going go be marked, this it used when generating the result string
gMarkingList = []
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
        #the string that is going to be outputted
        vResultString = []
        #temporary collections that are used in the actual solving
        vTempList = []
        #get duplicates from horizontal dictionary
        for i in range(gMatrixMaxInt+1):
                 if i in gMarkingDict_Horizontal:
                        vTempListGrouped = []
                         #get the  horizontal duplicates
                        vTempList = gMarkingDict_Horizontal[i].copy()
                        #no need to sort horizontal elements as they are inserted in the correct order (not going to sort them in order to be slightly more efficient hehe..)
                        #TODO - Create a more generic solution that groups n elements depending on their row/ e[1]                         
                        for j in range(len(vTempList)//2):
                                k=j*2
                                vTempListGrouped.append([vTempList[k], vTempList[k+1]])
                        for group in vTempListGrouped:
                                vHoldingList = []
                                for elem in group:
                                        #for each element in the group, we perform 3 tests, for each passed test the element is added to a temporary array, the element witht he largest count is the one which is prioritized
                                        #check if any of the elements share x axis with the vertical duplicates

                                        if not checkPlacement(elem): #does the element have any neighbors?
                                                break
                                        if checkVerticalDuplicates(elem, i): #does the element have any duplicates in y axis
                                                vHoldingList.append(elem)
                                        if checkPrefferentialPlacement(elem): #does the element have a prefferencial placement
                                                vHoldingList.append(elem)
                                if len(vHoldingList) > 1:
                                        #get the most frequent element in list
                                        v = most_frequent(vHoldingList)
                                        gMarkingList.append(v)
                                elif len(vHoldingList) == 1:
                                        gMarkingList.append(elem)                        
        #print the result in the requested format
        for y in range(gMatrixLength):
                for x in range(gMatrixLength):
                        #check if element is in markingList, if not get key from dictionary
                        if [x,y] in gMarkingList:
                                vResultString.append('x')
                        else:
                                vResultString.append(getKeyWithValue(pDict, [x,y]))
        return vResultString


# finds most frequent element in list or return either one based on some random calculation in case of equals
def most_frequent(List): 
    maxFrequency = 0
    vContenders = [] 
    
    #get element with highest frequency
    for element in List: 
        curr_frequency = List.count(element) 
        if(curr_frequency> maxFrequency): 
            maxFrequency = curr_frequency 
            mostFrequentElement = element 
  
    #now we have the highest frequency, check if there are any other entries with the same frequency
    for element in List:
        curr_frequency = List.count(element)
        if curr_frequency >= maxFrequency:
            if element not in vContenders:
                vContenders.append(element)
    #if there are several etries with the same frequency, then we just return the first one
    ramdonIndex = random.randrange(0, len(vContenders)-1)
    print(ramdonIndex)
    print(len(vContenders)-1)
    return vContenders[ramdonIndex]     
        



#Checks if the element has any dupicates in the vertical row
#Returns True if this is the case
def checkVerticalDuplicates(pElement, key):
        li = gMarkingDict_Vertical[key].copy()
        vResult = False
        #check if there are any entries in the vertical row that is not itself
        if pElement in li:
                li.remove(pElement)
        for l in li:
                if pElement[0] == l[0]:
                        vResult = True
        return vResult

#cheks if the element has any horizontal or vertial neighbors that have been mared
#Returns True if it does not breach the rule and the placement is OK
def checkPlacement(pElement):
        vResult = True
        for element in gMarkingList:
                if pElement[0] == element[0]+1:
                        vResult = False

                if pElement[0] == element[0]-1:
                        vResult = False

                if pElement[1] == element[1]+1:
                        vResult = False
                
                if pElement[1] == element[1]-1:
                        vResult = False
        return vResult


#checks if the element has a preferred placement, this being one of the corners
#This is because this reduces the change of blocking in some other non-marked element by the marked elements
#Returns True if the placement is preferred
def checkPrefferentialPlacement(pElement):
                vPreferredPlacements = [[0,0], [gMatrixLength-1,0], [0, gMatrixLength-1], [gMatrixLength-1, gMatrixLength-1]]
                if pElement in vPreferredPlacements:
                        return True
                else:
                        return False

#MAIN - Insturctions
# Either create a matrix by passing in numbers or generate one of any size
# Create the dictionaries that hold the horizontal and vertical duplicates
# run the solver on the dictioanry created from the matrix. The solver uses the marking dictionaries, it is therefore paramoutn that these are run beforehand 
def Main():
        vMatrix = createRandomMatrix(10, 10)
        vMatrix = createSpecificMatrix('5, 2, 1, 6, 2, 5', '3, 1, 4, 2, 6, 6', '4, 2, 3, 4, 6, 3', '4, 5, 6, 3 ,2, 2', '2, 4, 3, 3, 4, 5', '6, 4, 6, 5, 3, 3')
        print(vMatrix)
        vDictionary = decodeMatrix(vMatrix)
        markHorizontalDuplicates(vDictionary)
        markVerticalDuplicates(vDictionary)
        print(solver(vDictionary))

Main()
 
         
 