function first_missing_positive(list){
    let missing = 1
    for(let i = 1; i<=list.length; i++){
        if(!list.includes(i)){
            // return i
            break
        }
        missing += 1
    }

    return missing
}


console.log(first_missing_positive([1,2,3]))