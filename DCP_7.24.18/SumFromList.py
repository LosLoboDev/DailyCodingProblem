#date:7.24.18
#LosLoboDev

#returns a list of sums of the numbers in paramlist
def initSumsList(paramlist):

    list_of_sums = []

    i=0
    j=i+1
    while i < len(paramlist)-1:
        while j < len(paramlist):
            list_of_sums.append(paramlist[i] + paramlist[j])
            j+=1
        i+=1
        j=i+1

    return list_of_sums


#check if k is in paramlist
def isKInList(paramlist, k):

    returnVal = False
    
    if (paramlist.count(k) > 0):
        returnVal = True
    
    return returnVal


#main program
numsList1 = [10, 15, 3, 7]
k1=17
print("list={}".format(numsList1))
print("k={}".format(k1))
sumsList1 = initSumsList(numsList1)
print("sumsList={}".format(sumsList1))
print ("k is in the list of sums:{}\n".format(isKInList(sumsList1, k1)))

numsList2 = [10, 1, 35, 20]
k2=11
print("list={}".format(numsList2))
print("k={}".format(k2))
sumsList2 = initSumsList(numsList2)
print("sumsList={}".format(sumsList2))
print ("k is in the list of sums:{}\n".format(isKInList(sumsList2, k2)))

numsList3 = [10, 1, 35, 20, 9, 8, 23, 45, 64]
k3=56
print("list={}".format(numsList3))
print("k={}".format(k3))
sumsList3 = initSumsList(numsList3)
print("sumsList={}".format(sumsList3))
print ("k is in the list of sums:{}\n".format(isKInList(sumsList3, k3)))

numsList4 = []
k4=0
print("list={}".format(numsList4))
print("k={}".format(k4))
sumsList4 = initSumsList(numsList4)
print("sumsList={}".format(sumsList4))
print ("k is in the list of sums:{}\n".format(isKInList(sumsList4, k4)))