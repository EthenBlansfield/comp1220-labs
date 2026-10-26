comparisons = 0

    for i in range(1, len(items)):
        current = items[i]
        j = i - 1

        while j >= 0:
            comparisons += 1
            if items[j] <= current:
                break
            items[j + 1] = items[j]
            j -= 1

        items[j + 1] = current

        if show:
            print(items)

    return comparisons 


comparisons = 0 

    for i in range(1, len(items)): 
        current = items[i] 
        j = i - 1 

        while j >= 0:
            comparisons += 1 
            if items[j] <= current: 
                break 
            items[j + 1] = items[j] 
            j -= 1  

            items[ j + 1] = current 

            if show: 
                print(items) 

        return comparisons 

    
    

