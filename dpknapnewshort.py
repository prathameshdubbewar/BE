def knapsack(values,weights,capacity):
	
	n=len(values)
	dp=[0]*(capacity+1)

	for i in range(n):
		for w in range(capacity,0,-1):
			if weights[i]<=w:
				dp[w]=max(dp[w],dp[w-weights[i]]+values[i])
	return dp[capacity]

n=int(input("Enter the number of items: "))
values=[]
weights=[]

for i in range(n):
	value=int(input(f"Value of item{i+1}: "))
	weight=int(input(f"Weight of item{i+1}: "))
	values.append(value)
	weights.append(weight)

capacity=int(input("Enter the knapsack capacity: "))
max_value=knapsack(values,weights,capacity)
print(f"The maximum value that can be obtained is: {max_value}")