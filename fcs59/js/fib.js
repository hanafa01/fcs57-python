let n = 4

let a = 0
let b = 1

if(n < 0){
    console.log('Enter positive number')
}else if(n == 0){
    console.log(0)
}else{
    let result = ''
    for(let i = 0; i < n; i++){
        result += a + ' '
        let c = a + b
        a = b
        b = c
    }
    console.log(result)
}