a = int(input('base demand = '))
b = int(input('price sensitivity = '))
c = int(input('unit cost = '))

maxProfit = 0
optimalPrice = 0
for p in range(c+1 , a//b):
    profit = (a - b * p) * (p-c)
    #print(p, profit)
    
    if profit　> maxProfit:
        maxProfit = profit
        optimalPrice = p

print('optimal price = ' + str(optimalPrice))
print('maximized profit = ' + str(maxProfit))