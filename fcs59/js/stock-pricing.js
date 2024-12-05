function max_profit(prices){
    let profits = []
    for(let i = 1; i<prices.length; i++){
        if(prices[i] > prices[i-1]){
            profits.push(prices[i] - prices[i-1])
        }
    }

    return Math.max(profits)
}

console.log(max_profit([5,7,2]))