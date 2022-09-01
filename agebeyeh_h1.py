
def fib(num):
    listCalcualtedFib={}
    return findFibMemo(listCalcualtedFib, num)
def findFibMemo(listCalulatedFib, num):
    if num in listCalulatedFib:
        return listCalulatedFib[num]
    if num == 1:
        fibnum = num
        addCalculatedList(listCalulatedFib, num, fibnum)
        return 1
    elif num ==0:
        fibnum = num
        addCalculatedList(listCalulatedFib, num, fibnum)
        return 0
    else:
        fibnum = findFibMemo(listCalulatedFib, num-1) + findFibMemo(listCalulatedFib, num-2)
        addCalculatedList(listCalulatedFib, num, fibnum)
        return fibnum
    
def addCalculatedList(listCalculatedFib, num, fibNum):
    if fibNum not in listCalculatedFib:
        listCalculatedFib[num] = fibNum

def reversed(list):
    reversedList = []
    revNegLength = len(list) * -1
    index = -1
    while index >= revNegLength:
        reversedList.append(list[index])
        index -= 1
    return reversedList

def is_prime(num):
    bool = True
    if num <= 1 or countNumberDivisors(num) > 2:
        bool = False
    return bool

def countNumberDivisors(num):
    numberDivisors = 0
    for x in range(1, num+1):
        if num % x == 0:
            numberDivisors += 1
    return numberDivisors
def collatz(number):
    listSucessiveNumber =[]
    return recurFindSuccNum(number, listSucessiveNumber)

def recurFindSuccNum(number, listSuccesiveNumber):
    if number == 1:
        listSuccesiveNumber.append(number)
        return listSuccesiveNumber
    if number % 2 == 0:
        listSuccesiveNumber.append(number)
        number = number/2
        return recurFindSuccNum(number, listSuccesiveNumber)
    else:
        listSuccesiveNumber.append(number)
        number = number*3+1
        return recurFindSuccNum(number, listSuccesiveNumber)
def nub(list):
    if len(list) == 0:
        return list
    else:
        return removeDuplicate(list)
def removeDuplicate(list):
    listRemovedDuplicates=[]
    startIndex=0
    compareIndex= startIndex+1
    endIndex = len(list)-1
    while startIndex < len(list):
        if list[startIndex] in listRemovedDuplicates:
            startIndex+=1
            compareIndex+=1
        else:
            if compareIndex == endIndex and list[startIndex] not in listRemovedDuplicates:
                listRemovedDuplicates.append(list[startIndex])
                break
            if startIndex == endIndex and list[startIndex] not in listRemovedDuplicates:
                listRemovedDuplicates.append(list[startIndex])
                break
            if  list[startIndex] == list[compareIndex]:
                compareIndex+=1
            else:
                listRemovedDuplicates.append(list[startIndex])
                startIndex=compareIndex
                compareIndex+=1
    return listRemovedDuplicates 

def median(list):
    list.sort()
    indexBound = len(list)-1
    if len(list) % 2 == 0:
        index_midPoint_1 = int(indexBound/2)
        midPoint_1 = list[index_midPoint_1]
        midPoint_2 = list[index_midPoint_1+1]
        midPoint = (midPoint_1 + midPoint_2)/2
        return midPoint
    else:
        index_midPoint=int(indexBound/2)
        return list[index_midPoint]
def mode(list):
    list.sort()
    countEachNumberlist=findCountEachNumberList(list)
    ans=[]

def findCountEachNumberList(list):
    startIndex = 0
    compareIndex= startIndex+1
    count=0
    numberWithCount={}
    while(startIndex < len(list)):
        if compareIndex == len(list):
            count+=1
            number=list[startIndex]
            numberWithCount[number]=count
            count=0
            break
            
        else:
            if list[startIndex] == list[compareIndex]:
                count+=1
                compareIndex+=1
            else:
                count+=1
                number=list[startIndex]
                numberWithCount[number]=count
                startIndex = compareIndex
                compareIndex+=1
                count=0
    return numberWithCount

def zip_with(doOperation, input_1, input_2):
    numLength_input1= len(input_1)
    numLength_input2=len(input_2)
    if numLength_input1 == 0 :
        return input_1
    if numLength_input2 == 0 :
        return input_2
    inputSmallestLength=findInputSmallestLength(numLength_input1, numLength_input2)
    ans=[]
    index=0
    while(index < inputSmallestLength):
        resultOperation= doOperation(input_1[index], input_2[index])
        ans.append(resultOperation)
        index+=1
    return ans

def findInputSmallestLength(input1, input2):
    if input1 > input2:
        return input2
    elif input2 > input1:
        return input1
    else:
        return input1
