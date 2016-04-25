def change(coins,coin_count,amount):
    table = [[0 for x in range(coin_count)] for y in range(amount+1)]


    for i in range(coin_count):
        table[0][i] = 1

    for i in range(1,amount+1):
        for j in range(coin_count):
            x = table[i - coins[j]][j] if i - coins[j] >=0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x+y

    return table[amount][coin_count-1]


arr = [1,2,3]
m = len(arr)
amount = 7
print(change(arr,m,amount))
# combination (10 ones) (5 twos) (3 thress and one)
