prices = [7,1,5,3,6,4]
max_profit = 0
min_value = prices[0]
for i in range(1,len(prices)):
    min_value = min(min_value,prices[i])
    max_profit = max(max_profit,prices[i]-min_value)
print(max_profit)