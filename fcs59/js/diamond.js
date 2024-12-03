
let x = 5

for (let i = 1; i <= x; i++) {
    console.log(' '.repeat(x - i) + '*'.repeat(2 * i - 1))
}

for (let i = x - 1; i >= 1; i--) {
    console.log(' '.repeat(x - i) + '*'.repeat(2 * i - 1))
}