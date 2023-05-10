const prices = [1000, 500, 320, 1500, 2000];

// let total = 0 ;
// for(let price of prices){
//     total += price
// }

const result = prices.reduce((total, price) => {
    return total + price
})

const minPrice = prices.reduce((min, price) => {
    if (price < min){
        return price
    }
    return min
})