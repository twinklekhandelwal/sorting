def bubble_shorting(bubble_short):
    bubble_short=[3,6,8,2,9,1,11,54,32,23,99,88]
    i=0
    while(i<len(bubble_short)):
        j=0
        while(j<len(bubble_short)-1):
            if(bubble_short[j]>bubble_short[j+1]):
                tem=bubble_short[j+1]
                bubble_short[j+1]=bubble_short[j]
                bubble_short[j]=tem
            j=j+1 
        i=i+1

    return bubble_short          
bubble_list=[3,6,8,2,9,1,11,54,32,23,99,88]
print bubble_shorting(bubble_list)






