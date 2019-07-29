# O(t * n) 
from zero_one_knapsack import Items, KNAPSACK_SIZE, ITEM_AMOUNT
import random

RUN_TIMES = 200            # 随意算法运行次数


def monte_carlo(item_amount = ITEM_AMOUNT, knapsack_size = KNAPSACK_SIZE, run_times = RUN_TIMES):
    max_value = 0
    best_b = []
    for i in range(run_times):
        left_size = KNAPSACK_SIZE
        value = 0
        items = Items.copy()
        b = [0 for j in range(item_amount)]
        while True:
            item = random.choice(items)
            index = Items.index(item)
            items.remove(item)
            
            if item.getWeight() <= left_size:
                b[index] = 1
                left_size -= item.getWeight()
                value += item.getValue()
            else:
                break
        
        if value > max_value:
            max_value = value
            best_b = b.copy()

    
    print(best_b, "Run_times :", run_times, "Max value :", max_value)
    


if __name__ == "__main__":
    monte_carlo()