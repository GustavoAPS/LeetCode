
def canPlaceFlowers(flowerbed, n):
    """
    :type flowerbed: List[int]
    :type n: int
    :rtype: bool
    """


    #print(flowerbed)
    flowerbed.insert(0, 0)
    flowerbed.append(0)
    #print(flowerbed)

    flowers_planted = 0
        
  
    i = 1
    while i < len(flowerbed) - 1:
        #print(flowerbed[i])
        if flowerbed[i] == 0:
            if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
              flowerbed[i] = 1
              flowers_planted = flowers_planted + 1

        i = i + 1


    if flowers_planted >= n:
        return True
    else:
        return False
    
print(canPlaceFlowers([1,0,0,0,1],1))
print(canPlaceFlowers([1,0,0,0,1],2))