

class Directblock:
    index = 0
    offset = 0

    def __init__(self,index,offset):
        self.index = index
        self.offset = offset

    def binarySplit(self, number):
        s = str(bin(number))
        s = s[2:]
        if(self.index != 0):
            index = s[len(s)-self.offset-self.index:len(s)-self.offset]
        else:
            index = ""
        return [s[:len(s)-self.offset - self.index],index,s[len(s)-self.offset:len(s)]]


    def hexSplit(self,number):
        number = int(number)
        offset = hex(number % 2**self.offset)
        number = number//2**self.offset
        index = "" if self.index == 0 else hex(number%2**self.index)
        number = (number)//2**self.index
        return [hex(number)[2:],index[2:],offset[2:]]

    def printAll(self,numbers):
        for number in numbers:
            result = self.hexSplit(number)
            result.append((number//2**self.offset)%2**self.index)
            result.append(number)
            print(str(result))




if __name__ == "__main__":
    blocks = Directblock(8,7)
    blocks.printAll([1573,61440,57845,30000,49920,24976,61534])

