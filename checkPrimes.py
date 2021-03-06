import math
import random

class Prime:
    def isPrime(self, number):
        if number < 2:
            return False
        for i in range(2, int(math.sqrt(number)) + 1):
            if number % i == 0:
                return False
        return True

    def generatePrime(self, lowerLimit, upperLimit):
        primeList = []
        for i in range(lowerLimit, upperLimit):
            if self.isPrime(i):
                primeList.append(i)
        while True:
            randSelection = random.randint(0, len(primeList) + 1)
            if randSelection < len(primeList):
                return primeList[randSelection]

    def generatePrimitiveRoots(self, prime):
        allRoots = []
        for i in range(1, prime):
            allRootsPrimitiveRoots = []
            for j in range(0, prime - 1):
                if (pow(i, j) % prime) not in allRoots:
                    allRootsPrimitiveRoots.append(pow(i, j) % prime)
            allRoots.append(allRootsPrimitiveRoots)
        allRoots = list(set(allRoots)
        return allRoots[random.randint(0, len(allRoots) + 1)]