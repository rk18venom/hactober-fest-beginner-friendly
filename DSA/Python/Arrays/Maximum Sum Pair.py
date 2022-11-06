def findLargestSumPair(arr, n):
    if arr[0] > arr[1]:
        firstLargest = arr[0]
        secondLargest = arr[1]
 
    else:
        firstLargest = arr[1]
        secondLargest = arr[0]
 
    
    for i in range(2, n):
 
        
        if arr[i] > firstLargest:
            secondLargest = firstLargest
            firstLargest = arr[i]

        elif arr[i] > secondLargest and arr[i] != firstLargest:
            secondLargest = arr[i]
 
    return (firstLargest + secondLargest)