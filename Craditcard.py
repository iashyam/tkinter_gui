class Card():
    def __init__(self, number):
        self.number = (number)


    def sumDoubleEven(self):
        sum = 0
        for i in range(0, len(self.number),2):
            double = 2*(int(self.number[i]))
            if double>=10:
                double = str(double)
                double = int(double[0]) + int(double[1])
            sum += double
        return sum

    def sumOdd(self):
        sum = 0
        for i in range(1,len(self.number),2):
            sum += int(self.number[i])
        return sum

    def allSum(self):
        alls = self.sumOdd() + self.sumDoubleEven()
        return alls

    def Isvalid(self):
        if (self.allSum())%10 == 0:
            return True
        elif len(self.number) == 0:
            return False
        else:
            return False

# if __name__ == '__main__':
#
#     card_number = input("Enter Card Number: ")
#     card = Card(card_number)
#
#     if card.Isvalid():
#         print("This Card is valid: ")
#     else:
#         print(("This card is not valid."))