class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        planter = 0

        if len(flowerbed) == 1:
            if flowerbed[0] == 0:
                return 1 >= n
            else:
                return 0 == n
            

        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0:
                    if flowerbed[i + 1] == 0:
                        planter += 1
                        flowerbed[i] = 1
                elif i == len(flowerbed) - 1:
                    if flowerbed[i - 1] == 0:
                        planter += 1
                        flowerbed[i] = 1
                elif flowerbed[i + 1] == 0:
                    if flowerbed[i - 1] == 0:
                        planter += 1
                        flowerbed[i] = 1
        return planter >= n
                
        