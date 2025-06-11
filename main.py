import time

COINS = [50, 25, 10, 5, 2, 1]

# --- ЖАДІБНИЙ АЛГОРИТМ ---
def find_coins_greedy(amount):
    result = {}
    for coin in COINS:
        if amount >= coin:
            count = amount // coin
            result[coin] = count
            amount -= coin * count
    return result

# --- ДИНАМІЧНЕ ПРОГРАМУВАННЯ ---
def find_min_coins(amount):
    # dp[i] зберігає мінімальну кількість монет для суми i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 0 монет для суми 0

    # Для зберігання останнього використаного номіналу
    last_coin = [0] * (amount + 1)

    for coin in COINS:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                last_coin[i] = coin

    # Відновлення результату
    result = {}
    while amount > 0:
        coin = last_coin[amount]
        result[coin] = result.get(coin, 0) + 1
        amount -= coin
    return result

# --- ПЕРЕВІРКА ---
amount = 113

print("Жадібний алгоритм:")
start = time.time()
greedy_result = find_coins_greedy(amount)
end = time.time()
print("Результат:", greedy_result)
print("Час виконання:", round(end - start, 6), "секунд\n")

print("Динамічне програмування:")
start = time.time()
dp_result = find_min_coins(amount)
end = time.time()
print("Результат:", dp_result)
print("Час виконання:", round(end - start, 6), "секунд")
