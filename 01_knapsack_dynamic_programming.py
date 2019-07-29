# n * m
from zero_one_knapsack import Items, KNAPSACK_SIZE, ITEM_AMOUNT
import numpy as np 

max_weight_Item = { "arrange"   : [],
                    "weight"    : 0,
                    "value"     : 0}



def dynamic_programming(item_amount = ITEM_AMOUNT, knapsack_size = KNAPSACK_SIZE):
    c = np.zeros((item_amount, knapsack_size + 1), int)
    for w in range(1, knapsack_size + 1):
        for i in range(item_amount):
            if w < Items[i].getWeight():
                c[i][w] = c[i - 1][w]
            elif c[i -1 ][w - int(Items[i].getWeight())] + Items[i].getValue() > c[i - 1][w]:
                c[i][w] = c[i -1 ][w - int(Items[i].getWeight())] + Items[i].getValue()
            else:
                c[i][w] = c[i - 1][w]

        if c[i][w] > max_weight_Item['value']:
            max_weight_Item["value"] = c[i][w]

    print("max value",":", max_weight_Item["value"])

if __name__ == "__main__":
    dynamic_programming()