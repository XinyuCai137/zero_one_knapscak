class Item(object):
    def __init__(self, n, w, v):
        self.name=n
        self.weight=int(w)
        self.value=int(v)

    def getName(self):
        return self.name

    def getWeight(self):
        return self.weight

    def getValue(self):
        return self.value

    def __str__(self):
        result = ' < '+self.name+' , '+str(self.value)+' , '+str(self.weight) + '>'
        return result

KNAPSACK_SIZE = 100
ITEM_AMOUNT = 10

Weights =   (35, 30,  8, 20, 12, 40, 25,  5, 50, 10)
Values =    (30, 40, 15, 20, 10, 35, 30, 20, 75,  5)

Items = [ Item(i, Weights[i], Values[i]) for i in range(10)]

if __name__ == "__main__":
    for item in Items:
        print(item.getName(), item.getWeight(), item.getValue())