# O(2^n)
from zero_one_knapsack import Items, KNAPSACK_SIZE, ITEM_AMOUNT
def sort_max_united_value():
    united_value = []
    Items_ = []
    for i in range(ITEM_AMOUNT):
        united_value.append(Items[i].getValue() / Items[i].getWeight())
    
    united_value_ = []
    for i in range(ITEM_AMOUNT):
        index = united_value.index(max(united_value))
        value = united_value.pop(index)
        item = Items.pop(index)
        Items_.append(item)
        united_value_.append(value)

    for item in Items_:
        print(item.getName(), item.getWeight(), item.getValue())

    print(united_value_)
    return Items_, united_value_
    

def branch_and_bound(item_amount = ITEM_AMOUNT, knapsack_size = KNAPSACK_SIZE):
    items, united_value_s = sort_max_united_value()
    united_value_s.append(0)
    b_s = [[1], [0]]
    expect_value_s = [items[0].getValue() + (knapsack_size - items[0].getWeight()) * items[1].getValue(), knapsack_size * items[1].getValue()]
    max_value = 0
    best_b = []
    while len(b_s):
        left_size = knapsack_size
        value = 0
        b = b_s.pop(0)
        expect_value_s.pop(0)
        for i in range(len(b)):
            if b[i]:
                if items[i].getWeight() <= left_size:
                    value += items[i].getValue()
                    left_size -= items[i].getWeight()
            
            if max_value < value:
                best_b = b.copy()
                max_value = value
        if len(b) < item_amount:

            if items[len(b)].getWeight() <= left_size:
                j = len(b)
                expect_value = value
                while j < item_amount and items[j].getWeight() > left_size:
                    expect_value += items[j].getWeight()
                    j += 1
                if j < item_amount:
                    expect_value += left_size * united_value_s[j]

                j = 0
                for e in expect_value_s:
                    if expect_value < e: 
                        j += 1
                    else:
                        break
                expect_value_s.insert(j, expect_value) 
                b_s.insert(j, b + [1])

            j = len(b) + 1
            expect_value = value
            while j < item_amount and items[j].getWeight() > left_size:
                expect_value += items[j].getWeight()
                j += 1
            if j < item_amount:
                expect_value += left_size * united_value_s[j]
            
            j = 0
            for e in expect_value_s:
                if expect_value < e: 
                    j += 1
                else:
                    break
            if expect_value > max_value:
                expect_value_s.insert(j, expect_value) 
                b_s.insert(j, b + [0])

    print(best_b, "Max value :", max_value)

branch_and_bound()
