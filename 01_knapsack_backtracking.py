# O(2^n)
from zero_one_knapsack import Items, KNAPSACK_SIZE, ITEM_AMOUNT

max_weight_Item = { "arrange"   : [],
                    "weight"    : 0,
                    "value"     : 0}

value = 0
weight = 0
b = [0 for i in range(10)]

def backtracking(i):
    global value, weight
    j = i
    value_ = value
    while j < ITEM_AMOUNT:
        value_ += Items[j].getValue()
        j += 1
    if(i >= ITEM_AMOUNT or value_ < max_weight_Item["value"]):
        return

    b[i] = 0
    backtracking(i + 1)

    if(weight + Items[i].getWeight() <= KNAPSACK_SIZE):
        b[i] = 1
        weight += Items[i].getWeight()
        value += Items[i].getValue()
        print(b, '-', 'weight:', weight, 'value:', value)
        if value > max_weight_Item['value']:
            max_weight_Item["arrange"] = b.copy()
            max_weight_Item["weight"] = weight
            max_weight_Item["value"] = value
        backtracking(i + 1)
        weight -= Items[i].getWeight()
        value -= Items[i].getValue()
        b[i] = 0

if __name__ == "__main__":
    backtracking(0)
    print("Max value:")
    print(max_weight_Item["arrange"], '-', 'weight:', max_weight_Item["weight"], 'value:', max_weight_Item["value"])