from math import log
class block:

    def __init__(self,*args):
        self.splits = []
        for val in args:
            self.splits.append(val)
        self.splits.reverse()


    def hexSplit(self,number):
        results = []
        block_num = number // 2**(self.splits[-0])
        for split in self.splits:
            results.insert(0,hex(number % 2**split)[2:]) 
            number = number//2**split
        results.insert(0,hex(number)[2:])
        results.append(hex(block_num)[2:])
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

def indexOfNWay(size,way):
    return log(size/(64*way),2)

l = [block(23,7,6),block(24,6,6),block(21,9,6),block(19,11,6)]

def levels(number):
    for level in l:
        print(level.hexSplit(number))

if __name__ == "__main__":
    blocks = block(8,7)
    blocks.printAllHex(1573,61440,57845,30000,49920,24976,61534)
    print("")
    blocks = block(8,6)
    blocks.printAllHex(66000,66900,327600,132656,196500,198145,262596,327605,263746,329223)

    

