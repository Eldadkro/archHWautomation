class block:

    def __init__(self,*args):
        self.splits = []
        for val in args:
            self.splits.append(val)
        self.splits.reverse()


    def hexSplit(self,number):
        results = []
        for split in self.splits:
            results.insert(0,hex(number % 2**split)[2:]) 
            number = number//2**split
        results.insert(0,hex(number)[2:])
        return results


    def binSplit(self,number):
        results = []
        for split in self.splits:
            results.insert(0,bin(number % 2**split)[2:]) 
            number = number//2**split
        results.insert(0,bin(number)[2:])
        return results
    
    def printAllHex(self,*numbers):
        for number in numbers:
            result = self.hexSplit(number)
            result.append(number)
            print(str(result))

    def printAllBin(self,*numbers):
            for number in numbers:
                result = self.binSplit(number)
                result.append((number))
                print(str(result))


if __name__ == "__main__":
    blocks = block(10,6)
    blocks.printAllHex(66000,66900,327600,132656,196500,198145,26296,327605,263746,239223)

