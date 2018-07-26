#date:7.25.18
#LosLoboDev

#returns an array such that each element @ index i of the array
#is the product of all the numbers in the original array except
#the one @ index i.
#The resultant array will be of length len(originalArray-1)
#or of length = 0
def initProductsArray(originalArray):

    #handle edge cases
    #   1. only one element or empty array
    #   2. 2 element array
    if (len(originalArray) <= 1):
        return []
    elif (len(originalArray) == 2):
        product = originalArray[0]*originalArray[1]
        return [product]

    #create a new array of length len(originalArray-1)
    newArray = [0] * (len(originalArray)-1)

    i = 0
    j = 0
    product = 1
    while(i < len(originalArray)-1):
        while (j < len(originalArray)):
            if (j != i):
                product*=originalArray[j]
            j+=1
        #add element @ index i 
        #and reset product and inner loop counter
        newArray[i] = product
        #newArray.append(product)
        product = 1
        j=0
        i+=1
    return newArray


#main program
#tests
givenArray = [1, 2, 3, 4, 5]
productsArray = initProductsArray(givenArray)
print("givenArray = {}".format(givenArray))
print("resultant array = {}\n".format(productsArray))

givenArray = [3, 2, 1]
productsArray = initProductsArray(givenArray)
print("givenArray = {}".format(givenArray))
print("resultant array = {}\n".format(productsArray))

givenArray = [3, 2, 2, 2, 2]
productsArray = initProductsArray(givenArray)
print("givenArray = {}".format(givenArray))
print("resultant array = {}\n".format(productsArray))

givenArray = []
productsArray = initProductsArray(givenArray)
print("givenArray = {}".format(givenArray))
print("resultant array = {}\n".format(productsArray))

givenArray = [1]
productsArray = initProductsArray(givenArray)
print("givenArray = {}".format(givenArray))
print("resultant array = {}\n".format(productsArray))

givenArray = [4, 15]
productsArray = initProductsArray(givenArray)
print("givenArray = {}".format(givenArray))
print("resultant array = {}\n".format(productsArray))