function find_peaks(arr){
    let peaks = []
    for(let i = 1; i<arr.length; i++){
        if(arr[i] > arr[i-1] && arr[i] > arr[i+1]){
            peaks.push(i)
        }
    }

    return peaks
}

console.log(find_peaks([1,5,3,6,2,9]))