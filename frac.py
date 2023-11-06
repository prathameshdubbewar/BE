def fractional_knapsack(items, capacity):
    # Calculate the value-to-weight ratio for each item
    for item in items:
        item['ratio'] = item['value'] / item['weight']
    
    # Sort items based on the ratio in descending order
    items.sort(key=lambda x: x['ratio'], reverse=True)
    
    total_value = 0
    knapsack = []
    
    for item in items:
        if capacity >= item['weight']:
            # If the item can fit entirely in the knapsack, add it
            knapsack.append(item)
            total_value += item['value']
            capacity -= item['weight']
        else:
            # If the item cannot fit entirely, add a fraction of it
            fraction = capacity / item['weight']
            knapsack.append({'weight': capacity, 'value': item['value'] * fraction})
            total_value += item['value'] * fraction
            break
    
    return knapsack, total_value

# Example usage
items = [
    {'weight': 2, 'value': 10},
    {'weight': 3, 'value': 5},
    {'weight': 5, 'value': 15},
    {'weight': 7, 'value': 7},
    {'weight': 1, 'value': 6}
]

capacity = 10

knapsack, total_value = fractional_knapsack(items, capacity)
print("Selected items in the knapsack:")
for item in knapsack:
    print("Weight:", item['weight'], "Value:", item['value'])
print("Total value in the knapsack:", total_value)
