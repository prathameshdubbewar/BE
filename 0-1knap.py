# def knapsack(weights, values, capacity):
#     n = len(weights)
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
#     # Build the dp table using bottom-up dynamic programming
#     for i in range(1, n + 1):
#         for w in range(capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
#             else:
#                 dp[i][w] = dp[i - 1][w]
    
#     # Reconstruct the selected items
#     selected_items = []
#     i, w = n, capacity
#     while i > 0 and w > 0:
#         if dp[i][w] != dp[i - 1][w]:
#             selected_items.append(i - 1)
#             w -= weights[i - 1]
#         i -= 1
    
#     # Return the maximum value and the indices of selected items
#     return dp[n][capacity], selected_items[::-1]

# # Example usage
# weights = [2, 3, 4, 5]
# values = [3, 4, 5, 6]
# capacity = 5
# max_value, selected_items = knapsack(weights, values, capacity)
# print("Maximum value:", max_value)
# print("Selected items (indices):", selected_items)


def knapsack(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]

    # Track selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]

    return dp[n][capacity], selected_items[::-1]  # Reversed for correct order

n = int(input("Enter the number of items: "))
values = []
weights = []

for i in range(n):
    value = int(input(f"Value of item {i + 1}: "))
    weight = int(input(f"Weight of item {i + 1}: "))
    values.append(value)
    weights.append(weight)

capacity = int(input("Enter the knapsack capacity: "))
max_value, selected_items_indices = knapsack(values, weights, capacity)

selected_values = [values[i] for i in selected_items_indices]
selected_weights = [weights[i] for i in selected_items_indices]

print(f"The maximum value that can be obtained is: {max_value}")
print(f"Selected items' values: {selected_values}")
print(f"Selected items' weights: {selected_weights}")
