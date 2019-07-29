# n * 2^n
from zero_one_knapsack import Items, KNAPSACK_SIZE, ITEM_AMOUNT

b = 0b1

Bin = [(b << i) for i in range(ITEM_AMOUNT)]

max_weight_Item = { "arrange"   : 0,
                    "weight"    : 0,
                    "value"     : 0}

def proof_by_exhaustion():
    for i in range(b << ITEM_AMOUNT):
        weight = 0
        value = 0
        for j in range(ITEM_AMOUNT):
            if(Bin[j] & i):
                weight += Items[j].getWeight()
                value += Items[j].getValue()

        if weight > KNAPSACK_SIZE:
            # print('%12s' % bin(i), '-', 'Invalid')
            pass
        else:
            print('%12s' % bin(i), '-', 'weight:', weight, 'value:', value)
            if value > max_weight_Item['value']:
                max_weight_Item["arrange"] = i
                max_weight_Item["weight"] = weight
                max_weight_Item["value"] = value

    print("Max value:")
    print('%12s' % bin(max_weight_Item["arrange"]), '-', 'weight:', max_weight_Item["weight"], 'value:', max_weight_Item["value"])


if __name__ == "__main__":
    proof_by_exhaustion()
