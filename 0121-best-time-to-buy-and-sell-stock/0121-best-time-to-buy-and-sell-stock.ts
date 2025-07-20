function maxProfit(prices: number[]): number {
    // 풀이
    // 1. 최소값을 구해나가면서 최대 이익을 계산해나간다.
    var min_price: number = 10000 + 1
    var max_profit: number = 0

    for (const price of prices) {
        if (min_price > price) {
            min_price = price
        }
        if (max_profit < price - min_price) {
            max_profit = price - min_price
        }
    }

    return max_profit > 0 ? max_profit : 0
};