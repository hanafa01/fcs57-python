def find_peaks(array):
    peaks = []
    for i in range(1, len(array) - 1):
        if array[i] > array[i-1] and array[i] > array[i+1]:
            peaks.append(i)
        
    return peaks

print(find_peaks([1,5,3,6,2,9]))