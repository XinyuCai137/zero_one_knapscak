# O(n * m)
from zero_one_knapsack import Items, KNAPSACK_SIZE, ITEM_AMOUNT
import numpy as np 

c = np.zeros((ITEM_AMOUNT + 1, KNAPSACK_SIZE + 1), int)
count = 0

def memorandum(item_amount = ITEM_AMOUNT, knapsack_size = KNAPSACK_SIZE):
    global count
    count += 1
    print(count)
    if item_amount <= 0:
        return 0

    value_1 = 0
    value_2 = 0
    
    if c[item_amount - 1][knapsack_size]:
        value_1 = c[item_amount - 1][knapsack_size]
    else:
        value_1 = memorandum(item_amount - 1, knapsack_size)

    if knapsack_size - Items[item_amount-1].getWeight() < 0:
        c[item_amount][knapsack_size] = value_1
    else:
        if c[item_amount - 1][knapsack_size - Items[item_amount-1].getWeight()]:
            value_2 = c[item_amount - 1][knapsack_size - Items[item_amount-1].getWeight()] \
                + Items[item_amount-1].getValue()
        else:
            value_2 = memorandum(item_amount - 1, knapsack_size - Items[item_amount-1].getWeight()) \
                + Items[item_amount-1].getValue()

        if value_1 < value_2:
            c[item_amount][knapsack_size] = value_2

        else:
            c[item_amount][knapsack_size] = value_1

    return c[item_amount][knapsack_size]

if __name__ == "__main__":
    print("max value",":", memorandum())