function special_rearrangement(nums){
    let l_even = []
    let l_odd = []

    for(let x of nums){
        if(x % 2 == 0){
            l_even.push(x)
        }else{
            l_odd.push(x)
        }
    }

    return l_even.concat(l_odd)
}

console.log(special_rearrangement([1,2,4,6,2,1,3,7,9,10]))